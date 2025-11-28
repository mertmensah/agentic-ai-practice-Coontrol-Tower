import React, { useState, useRef, useEffect } from 'react'
import { processPipeline, translateToCat, moderateContent } from '../services/api'

function ChatInterface() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSend = async () => {
    if (!input.trim()) return

    const userInput = input.trim()
    
    // Add user message
    const userMessage = { role: 'user', content: userInput }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      // Send to multi-agent pipeline
      const response = await processPipeline(userInput)
      
      // Add agent response with the final cat translation
      const agentMessage = { 
        role: 'agent', 
        content: response.final_output || 'Processing complete!'
      }
      setMessages(prev => [...prev, agentMessage])
    } catch (error) {
      console.error('Error:', error)
      const errorMessage = { 
        role: 'error', 
        content: 'Failed to connect to agent system. Please check if the backend is running.'
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="chat-interface">
      <div className="chat-messages">
        {messages.length === 0 && (
          <div className="empty-state">
            <div className="empty-state-icon">🐱</div>
            <h3>Welcome to Agentic AI</h3>
            <p>
              Your message will be checked for appropriateness, then translated to cat language. 
              Type something to get started!
            </p>
          </div>
        )}
        
        {messages.map((msg, idx) => (
          <div key={idx} className={`message message-${msg.role}`}>
            <strong>{msg.role === 'user' ? 'You' : msg.role === 'agent' ? 'AI Agent' : 'Error'}</strong>
            <p>{msg.content}</p>
          </div>
        ))}
        
        {loading && (
          <div className="message message-loading">
            <strong>AI Agent</strong>
            <p>Processing through agents...</p>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
      
      <div className="chat-input">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message here..."
          disabled={loading}
          rows={1}
        />
        <button onClick={handleSend} disabled={loading || !input.trim()}>
          {loading ? 'Processing...' : 'Send'}
        </button>
      </div>
    </div>
  )
}

export default ChatInterface
