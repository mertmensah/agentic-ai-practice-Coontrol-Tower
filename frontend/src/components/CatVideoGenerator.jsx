import React, { useState } from 'react'
import { generateCatVideo } from '../services/api'

function CatVideoGenerator() {
  const [imageFile, setImageFile] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const handleImageUpload = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImageFile(file)
      
      // Create preview
      const reader = new FileReader()
      reader.onloadend = () => {
        setImagePreview(reader.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleGenerate = async () => {
    if (!imageFile) return

    setLoading(true)
    try {
      const formData = new FormData()
      formData.append('image', imageFile)

      const response = await generateCatVideo(formData)
      setResult(response)
    } catch (error) {
      console.error('Error:', error)
      setResult({ error: 'Failed to generate video' })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="cat-video-module">
      <div className="module-header">
        <h1>🎬 Cat Video Generator</h1>
        <p>Transform static cat images into dynamic videos and GIFs</p>
      </div>

      <div className="video-generator-section">
        <div className="upload-panel">
          <div className="upload-area">
            {!imagePreview ? (
              <label htmlFor="video-image" className="upload-placeholder">
                <div className="upload-icon">📸</div>
                <h3>Upload a Cat Image</h3>
                <p>Click to select or drag and drop</p>
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleImageUpload}
                  id="video-image"
                  style={{ display: 'none' }}
                />
              </label>
            ) : (
              <div className="preview-container">
                <img src={imagePreview} alt="Preview" className="image-preview" />
                <button onClick={() => { setImageFile(null); setImagePreview(null); }} className="remove-btn">
                  ✕ Remove
                </button>
              </div>
            )}
          </div>

          {imageFile && (
            <div className="generation-options">
              <h3>Video Options</h3>
              <div className="option-group">
                <label>
                  <input type="radio" name="format" value="video" defaultChecked />
                  <span>🎥 Video (MP4)</span>
                </label>
                <label>
                  <input type="radio" name="format" value="gif" />
                  <span>🌀 Animated GIF</span>
                </label>
              </div>

              <button
                onClick={handleGenerate}
                disabled={loading}
                className="generate-btn"
              >
                {loading ? '🎬 Generating...' : '🎞️ Generate Video'}
              </button>
            </div>
          )}
        </div>

        <div className="result-panel">
          {loading && (
            <div className="loading-state">
              <div className="spinner">🎬</div>
              <p>Animating your cat...</p>
              <small>This may take 10-30 seconds</small>
            </div>
          )}

          {result && !loading && (
            <div className="video-result">
              {result.video_url ? (
                <>
                  <video controls className="generated-video" autoPlay loop>
                    <source src={result.video_url} type="video/mp4" />
                    Your browser does not support video playback.
                  </video>
                  <div className="result-actions">
                    <button className="download-btn">⬇️ Download</button>
                    <button className="share-btn">🔗 Share</button>
                  </div>
                  {result.breed_match && (
                    <div className="breed-info">
                      <strong>🐾 Detected Breed:</strong> {result.breed_match}
                    </div>
                  )}
                </>
              ) : (
                <div className="error-state">
                  <p>{result.error || 'Failed to generate video'}</p>
                </div>
              )}
            </div>
          )}

          {!result && !loading && (
            <div className="empty-state">
              <div className="empty-icon">🎞️</div>
              <h3>Video Preview</h3>
              <p>Upload an image to create an animated cat video</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default CatVideoGenerator