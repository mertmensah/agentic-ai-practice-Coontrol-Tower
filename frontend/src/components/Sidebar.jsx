import React, { useState } from 'react'

function Sidebar({ currentPage, onNavigate, isCollapsed, onToggleCollapse }) {
  const menuItems = [
    { id: 'coontrol-tower', name: 'Coontrol Tower', icon: '🏠', description: 'Dashboard' },
    { id: 'text-to-cat', name: 'Text/Speech to Cat', icon: '🗣️', description: 'Voice & Text' },
    { id: 'dream-cat', name: 'Dream Cat Generator', icon: '🎨', description: 'AI Cat Images' },
    { id: 'cat-video', name: 'Cat Video Generator', icon: '🎬', description: 'AI Cat Videos' },
  ]

  return (
    <div className={`sidebar ${isCollapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        <button className="sidebar-toggle" onClick={onToggleCollapse}>
          {isCollapsed ? '☰' : '✕'}
        </button>
        {!isCollapsed && (
          <div className="sidebar-brand">
            <span className="brand-icon">😺</span>
            <span className="brand-text">Cat Platform</span>
          </div>
        )}
      </div>

      <nav className="sidebar-nav">
        {menuItems.map((item) => (
          <button
            key={item.id}
            className={`nav-item ${currentPage === item.id ? 'active' : ''}`}
            onClick={() => onNavigate(item.id)}
            title={isCollapsed ? item.name : ''}
          >
            <span className="nav-icon">{item.icon}</span>
            {!isCollapsed && (
              <div className="nav-content">
                <span className="nav-name">{item.name}</span>
                <span className="nav-desc">{item.description}</span>
              </div>
            )}
          </button>
        ))}
      </nav>

      {!isCollapsed && (
        <div className="sidebar-footer">
          <div className="status-indicator">
            <span className="status-dot"></span>
            <span>All Systems Online</span>
          </div>
        </div>
      )}
    </div>
  )
}

export default Sidebar