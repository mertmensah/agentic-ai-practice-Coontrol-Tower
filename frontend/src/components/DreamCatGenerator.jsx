import React, { useState } from 'react'
import { generateDreamCat } from '../services/api'

function DreamCatGenerator() {
  const [prompt, setPrompt] = useState('')
  const [imageFile, setImageFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const handleGenerate = async () => {
    if (!prompt.trim() && !imageFile) return

    setLoading(true)
    setResult(null) // Clear previous result
    try {
      const formData = new FormData()
      formData.append('prompt', prompt)
      if (imageFile) {
        formData.append('image', imageFile)
      }

      const response = await generateDreamCat(formData)
      
      // Check if generation was successful
      if (response.status === 'success' && response.image_url) {
        setResult(response)
      } else if (response.error) {
        setResult({ error: response.error })
      } else {
        setResult({ error: response.message || 'Failed to generate image' })
      }
    } catch (error) {
      console.error('Error:', error)
      setResult({ 
        error: error.response?.data?.error || error.message || 'Failed to generate cat image. Please try again.' 
      })
    } finally {
      setLoading(false)
    }
  }

  const handleImageUpload = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImageFile(file)
    }
  }

  return (
    <div className="dream-cat-module">
      <div className="module-header">
        <h1>🎨 Dream Cat Generator</h1>
        <p>Bring your perfect cat to life with AI-powered image generation</p>
      </div>

      <div className="generator-section">
        <div className="input-panel">
          <div className="input-group">
            <label>Describe Your Dream Cat</label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="A fluffy orange tabby cat with green eyes, sitting on a windowsill at sunset..."
              rows={4}
            />
          </div>

          <div className="input-group">
            <label>Reference Image (Optional)</label>
            <div className="file-upload">
              <input
                type="file"
                accept="image/*"
                onChange={handleImageUpload}
                id="cat-image"
              />
              <label htmlFor="cat-image" className="upload-btn">
                📷 Upload Image
              </label>
              {imageFile && <span className="file-name">{imageFile.name}</span>}
            </div>
          </div>

          <button
            onClick={handleGenerate}
            disabled={loading || (!prompt.trim() && !imageFile)}
            className="generate-btn"
          >
            {loading ? '🎨 Generating...' : '✨ Generate Dream Cat'}
          </button>
        </div>

        <div className="preview-panel">
          {loading && (
            <div className="loading-state">
              <div className="spinner">🐾</div>
              <p>Creating your dream cat...</p>
            </div>
          )}

          {result && !loading && (
            <div className="result-display">
              {result.error ? (
                <div className="error-state">
                  <div className="error-icon">❌</div>
                  <h3>Generation Failed</h3>
                  <p>{result.error}</p>
                  <button onClick={() => setResult(null)} className="retry-btn">
                    🔄 Try Again
                  </button>
                </div>
              ) : result.image_url ? (
                <>
                  <img src={result.image_url} alt="Generated Cat" className="generated-image" />
                  <div className="result-info">
                    <h3>😻 Your Dream Cat!</h3>
                    {result.enhanced_prompt && (
                      <p className="enhanced-prompt">
                        <strong>🎨 Enhanced Prompt:</strong> {result.enhanced_prompt}
                      </p>
                    )}
                    {result.breed_match && (
                      <p className="breed-info">
                        <strong>🐾 Breed Match:</strong> {result.breed_match}
                      </p>
                    )}
                    {result.moderation && (
                      <p className="moderation-info">✅ Content approved</p>
                    )}
                    <button onClick={() => setResult(null)} className="retry-btn">
                      🎨 Generate Another
                    </button>
                  </div>
                </>
              ) : (
                <div className="error-state">
                  <p>Unexpected error - no image generated</p>
                </div>
              )}
            </div>
          )}

          {!result && !loading && (
            <div className="empty-state">
              <div className="empty-icon">🖼️</div>
              <h3>Your Dream Cat Will Appear Here</h3>
              <p>Describe your perfect cat and watch AI bring it to life</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default DreamCatGenerator