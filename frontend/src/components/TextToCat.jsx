import React, { useState, useRef, useEffect } from 'react'
import { speechToCat, textToSpeech } from '../services/api'

function TextToCat() {
  const [input, setInput] = useState('')
  const [isRecording, setIsRecording] = useState(false)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [audioUrl, setAudioUrl] = useState(null)
  const [speechSupported, setSpeechSupported] = useState(false)
  const recognitionRef = useRef(null)

  // Check if Web Speech API is supported
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    if (SpeechRecognition) {
      setSpeechSupported(true)
      const recognition = new SpeechRecognition()
      recognition.continuous = false
      recognition.interimResults = false
      recognition.lang = 'en-US'

      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript
        setInput(transcript)
        setIsRecording(false)
      }

      recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error)
        setIsRecording(false)
        alert(`Speech recognition error: ${event.error}`)
      }

      recognition.onend = () => {
        setIsRecording(false)
      }

      recognitionRef.current = recognition
    }
  }, [])

  const handleTextSubmit = async () => {
    if (!input.trim()) return

    setLoading(true)
    try {
      const response = await speechToCat(input, 'text')
      setResult(response)

      // Generate audio if available
      if (response.cat_translation) {
        const audioResponse = await textToSpeech(response.cat_translation)
        setAudioUrl(audioResponse.audio_url)
      }
    } catch (error) {
      console.error('Error:', error)
      setResult({ error: 'Failed to process request' })
    } finally {
      setLoading(false)
    }
  }

  const handleVoiceRecord = async () => {
    if (!speechSupported) {
      alert('🎤 Speech recognition is not supported in your browser. Please use Chrome, Edge, or Safari.')
      return
    }

    if (isRecording) {
      // Stop recording
      recognitionRef.current.stop()
      setIsRecording(false)
    } else {
      // Start recording
      try {
        recognitionRef.current.start()
        setIsRecording(true)
      } catch (error) {
        console.error('Error starting speech recognition:', error)
        alert('Failed to start speech recognition. Please check microphone permissions.')
      }
    }
  }

  return (
    <div className="text-to-cat-module">
      <div className="module-header">
        <h1>🗣️ Text/Speech to Cat</h1>
        <p>Communicate with your feline friends in their native language</p>
      </div>

      <div className="input-section">
        <div className="input-modes">
          <button className="mode-btn active">📝 Text</button>
          <button 
            className={`mode-btn ${isRecording ? 'recording' : ''}`} 
            onClick={handleVoiceRecord}
            disabled={!speechSupported}
            title={!speechSupported ? 'Speech not supported in this browser' : 'Click to record'}
          >
            {isRecording ? '⏹️ Stop Recording' : '🎤 Voice'}
          </button>
        </div>

        <div className="text-input-area">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={isRecording ? "🎤 Listening..." : "Type something to translate to cat language..."}
            rows={4}
            disabled={isRecording}
          />
          <div className="input-actions">
            <button
              onClick={handleTextSubmit}
              disabled={loading || !input.trim() || isRecording}
              className="submit-btn"
            >
              {loading ? '🐾 Translating...' : '🐱 Translate to Cat'}
            </button>
          </div>
        </div>
      </div>

      {result && (
        <div className="result-section">
          <div className="result-card">
            <h3>📋 Your Input</h3>
            <p>{result.original_text || input}</p>
          </div>

          {result.moderation && (
            <div className="result-card moderation">
              <h3>🛡️ Content Check</h3>
              <p>{result.moderation.analysis}</p>
            </div>
          )}

          <div className="result-card translation">
            <h3>😺 Cat Translation</h3>
            <p className="cat-text">{result.cat_translation || result.final_output}</p>
          </div>

          {audioUrl && (
            <div className="result-card audio">
              <h3>🔊 Listen</h3>
              <audio controls src={audioUrl}>
                Your browser does not support audio playback.
              </audio>
            </div>
          )}
        </div>
      )}

      {!result && (
        <div className="empty-state">
          <div className="empty-icon">🐈</div>
          <h3>Ready to Meow!</h3>
          <p>Enter text above to hear what your cat would say</p>
        </div>
      )}
    </div>
  )
}

export default TextToCat