"""
Main Flask application for Agentic AI backend
Cat Management Platform with Multiple Modules
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from agents.orchestrator import MultiAgentOrchestrator
from agents.breed_match_agent import BreedMatchAgent
from agents.image_generation_agent import ImageGenerationAgent
from agents.video_generation_agent import VideoGenerationAgent

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:3000",
    "https://mertmensah.github.io"
])  # Enable CORS for frontend communication

# Initialize agents
orchestrator = MultiAgentOrchestrator()
breed_matcher = BreedMatchAgent()
image_generator = ImageGenerationAgent()
video_generator = VideoGenerationAgent()

@app.route('/')
def home():
    return jsonify({
        "message": "Cat Management Platform API",
        "status": "running",
        "modules": [
            "Coontrol Tower",
            "Text/Speech to Cat",
            "Dream Cat Generator",
            "Cat Video Generator"
        ]
    })

# ========================================
# Text/Speech to Cat Module Endpoints
# ========================================

@app.route('/api/text-to-cat', methods=['POST'])
def text_to_cat():
    """
    Convert text/speech to cat language with moderation
    """
    data = request.json
    input_text = data.get('text', '')
    input_type = data.get('type', 'text')  # 'text' or 'speech'
    
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    # Process through pipeline (moderation + translation)
    result = orchestrator.process_pipeline(input_text, skip_moderation=False)
    
    return jsonify(result)

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    """
    Convert cat language text to speech (TTS)
    """
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Placeholder for TTS integration
    return jsonify({
        "audio_url": None,
        "message": "Text-to-speech coming soon!",
        "text": text
    })

# ========================================
# Dream Cat Generator Module Endpoints
# ========================================

@app.route('/api/dream-cat/generate', methods=['POST'])
def generate_dream_cat():
    """
    Generate AI cat image from text prompt and/or reference image
    """
    prompt = request.form.get('prompt', '')
    image_file = request.files.get('image', None)
    
    if not prompt and not image_file:
        return jsonify({"error": "Provide prompt or image"}), 400
    
    # Use prompt or generate from image description
    if not prompt:
        prompt = "a beautiful cat"
    
    # Step 1: Moderate content
    moderation = orchestrator.process_single_agent(prompt, "moderator")
    
    # Check if content is appropriate
    if moderation and "not appropriate" in moderation.get('analysis', '').lower():
        return jsonify({
            "error": "Content not appropriate",
            "moderation": moderation
        }), 400
    
    # Step 2: Match breed if description provided
    breed_match = None
    if prompt:
        try:
            breed_result = breed_matcher.process(prompt)
            breed_match = breed_result.get('breed_analysis')
        except Exception as e:
            print(f"Breed matching error: {e}")
            breed_match = "Could not determine breed"
    
    # Step 3: Generate image using Hugging Face
    try:
        image_result = image_generator.generate_image(prompt)
        
        return jsonify({
            "image_url": image_result.get('image_url'),
            "prompt": prompt,
            "enhanced_prompt": image_result.get('enhanced_prompt'),
            "breed_match": breed_match,
            "moderation": moderation,
            "status": image_result.get('status'),
            "message": image_result.get('message')
        })
    except Exception as e:
        return jsonify({
            "error": f"Image generation failed: {str(e)}",
            "prompt": prompt
        }), 500

# ========================================
# Cat Video Generator Module Endpoints
# ========================================

@app.route('/api/cat-video/generate', methods=['POST'])
def generate_cat_video():
    """
    Generate animated video/GIF from cat image
    """
    image_file = request.files.get('image', None)
    format_type = request.form.get('format', 'mp4')
    
    if not image_file:
        return jsonify({"error": "No image provided"}), 400
    
    # Save uploaded image temporarily
    image_path = f"/tmp/{image_file.filename}"
    # image_file.save(image_path)  # Uncomment in production
    
    # Generate video
    video_result = video_generator.generate_video(image_path, format_type)
    
    # Optional: Detect breed from image
    breed_match = "Breed detection from image coming soon!"
    
    return jsonify({
        "video_url": video_result.get('video_url'),
        "format": format_type,
        "breed_match": breed_match,
        "status": "generated"
    })

# ========================================
# Breed Matching Endpoint
# ========================================

@app.route('/api/breed-match', methods=['POST'])
def match_breed():
    """
    Identify cat breed from description
    """
    data = request.json
    description = data.get('description', '')
    
    if not description:
        return jsonify({"error": "No description provided"}), 400
    
    result = breed_matcher.process(description)
    
    return jsonify(result)

# ========================================
# Legacy Endpoints (for compatibility)
# ========================================

@app.route('/api/agents/info', methods=['GET'])
def agents_info():
    """
    Get information about all available agents
    """
    return jsonify(orchestrator.get_agents_info())

@app.route('/api/agents/pipeline', methods=['POST'])
def process_pipeline():
    """
    Process text through the full agent pipeline
    """
    data = request.json
    input_text = data.get('text', '')
    skip_moderation = data.get('skip_moderation', False)
    
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    result = orchestrator.process_pipeline(input_text, skip_moderation)
    
    return jsonify(result)

@app.route('/api/agent/status', methods=['GET'])
def agent_status():
    """
    Check agent status
    """
    return jsonify({
        "status": "active",
        "system": "Cat Management Platform",
        "agents_available": 6,
        "modules": 4
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
