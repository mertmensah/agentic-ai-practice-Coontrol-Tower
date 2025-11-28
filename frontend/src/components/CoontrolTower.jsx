import React, { useState, useEffect } from 'react'

function CoontrolTower() {
  const [currentDate, setCurrentDate] = useState(new Date())

  useEffect(() => {
    const timer = setInterval(() => setCurrentDate(new Date()), 1000)
    return () => clearInterval(timer)
  }, [])

  const modules = [
    {
      id: 'text-to-cat',
      name: 'Text/Speech to Cat',
      icon: '🗣️',
      description: 'Convert your voice or text into adorable cat language',
      stats: { requests: 128, success: '98%' },
      color: '#05C167'
    },
    {
      id: 'dream-cat',
      name: 'Dream Cat Generator',
      icon: '🎨',
      description: 'Generate AI-powered images of your dream cat',
      stats: { generated: 47, rating: '4.8/5' },
      color: '#276EF1'
    },
    {
      id: 'cat-video',
      name: 'Cat Video Generator',
      icon: '🎬',
      description: 'Transform cat images into dynamic videos and GIFs',
      stats: { videos: 23, duration: '~5s' },
      color: '#E91E63'
    }
  ]

  const formatDate = (date) => {
    return date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  }

  const formatTime = (date) => {
    return date.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    })
  }

  return (
    <div className="coontrol-tower">
      <div className="tower-header">
        <div className="header-content">
          <h1>🐱 Coontrol Tower</h1>
          <p className="subtitle">Your Cat Management Command Center</p>
        </div>
        <div className="date-time-display">
          <div className="date">{formatDate(currentDate)}</div>
          <div className="time">{formatTime(currentDate)}</div>
        </div>
      </div>

      <div className="welcome-section">
        <div className="welcome-card">
          <h2>Welcome Back! 👋</h2>
          <p>
            All systems are operational and ready to transform your ideas into purr-fect creations.
            Select a module below to get started.
          </p>
        </div>
      </div>

      <div className="modules-grid">
        {modules.map((module) => (
          <div key={module.id} className="module-card" style={{ borderLeftColor: module.color }}>
            <div className="module-icon">{module.icon}</div>
            <div className="module-info">
              <h3>{module.name}</h3>
              <p>{module.description}</p>
              <div className="module-stats">
                {Object.entries(module.stats).map(([key, value]) => (
                  <div key={key} className="stat">
                    <span className="stat-label">{key}:</span>
                    <span className="stat-value">{value}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="module-status">
              <span className="status-badge active">Active</span>
            </div>
          </div>
        ))}
      </div>

      <div className="system-info">
        <div className="info-card">
          <span className="info-icon">🛡️</span>
          <div>
            <strong>Content Moderation</strong>
            <p>All inputs are automatically checked for appropriateness</p>
          </div>
        </div>
        <div className="info-card">
          <span className="info-icon">🐾</span>
          <div>
            <strong>Breed Matching</strong>
            <p>AI-powered cat breed identification and suggestions</p>
          </div>
        </div>
        <div className="info-card">
          <span className="info-icon">⚡</span>
          <div>
            <strong>Fast Processing</strong>
            <p>Powered by Google Gemini 2.5 for instant results</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default CoontrolTower