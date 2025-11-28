/**
 * API Service for Cat Management Platform
 * Multi-Module System API
 */
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 90000, // 90 second timeout for AI image generation
})

// ========================================
// Text/Speech to Cat Module
// ========================================

/**
 * Convert text or speech to cat language
 */
export const speechToCat = async (text, type = 'text') => {
  const response = await api.post('/api/text-to-cat', { text, type })
  return response.data
}

/**
 * Convert text to speech audio
 */
export const textToSpeech = async (text) => {
  const response = await api.post('/api/text-to-speech', { text })
  return response.data
}

// ========================================
// Dream Cat Generator Module
// ========================================

/**
 * Generate AI cat image from prompt and/or reference image
 */
export const generateDreamCat = async (formData) => {
  const response = await api.post('/api/dream-cat/generate', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    timeout: 120000, // 2 minutes for image generation (first time can be slow)
  })
  return response.data
}

// ========================================
// Cat Video Generator Module
// ========================================

/**
 * Generate animated video/GIF from cat image
 */
export const generateCatVideo = async (formData) => {
  const response = await api.post('/api/cat-video/generate', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })
  return response.data
}

// ========================================
// Breed Matching
// ========================================

/**
 * Identify cat breed from description
 */
export const matchBreed = async (description) => {
  const response = await api.post('/api/breed-match', { description })
  return response.data
}

// ========================================
// Legacy/Original Endpoints
// ========================================

/**
 * Process text through the full agent pipeline
 */
export const processPipeline = async (text, skipModeration = false) => {
  const response = await api.post('/api/agents/pipeline', { 
    text, 
    skip_moderation: skipModeration 
  })
  return response.data
}

/**
 * Translate text to cat language
 */
export const translateToCat = async (text) => {
  const response = await api.post('/api/agents/translate', { text })
  return response.data
}

/**
 * Check if content is workplace appropriate
 */
export const moderateContent = async (text) => {
  const response = await api.post('/api/agents/moderate', { text })
  return response.data
}

/**
 * Get information about available agents
 */
export const getAgentsInfo = async () => {
  const response = await api.get('/api/agents/info')
  return response.data
}

/**
 * Check agent status
 */
export const getAgentStatus = async () => {
  const response = await api.get('/api/agent/status')
  return response.data
}

export default api
