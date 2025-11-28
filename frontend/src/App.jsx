import React, { useState } from 'react'
import Sidebar from './components/Sidebar'
import CoontrolTower from './components/CoontrolTower'
import TextToCat from './components/TextToCat'
import DreamCatGenerator from './components/DreamCatGenerator'
import CatVideoGenerator from './components/CatVideoGenerator'
import './styles/App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('coontrol-tower')
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)

  const renderPage = () => {
    switch (currentPage) {
      case 'coontrol-tower':
        return <CoontrolTower />
      case 'text-to-cat':
        return <TextToCat />
      case 'dream-cat':
        return <DreamCatGenerator />
      case 'cat-video':
        return <CatVideoGenerator />
      default:
        return <CoontrolTower />
    }
  }

  return (
    <div className="App">
      <Sidebar
        currentPage={currentPage}
        onNavigate={setCurrentPage}
        isCollapsed={sidebarCollapsed}
        onToggleCollapse={() => setSidebarCollapsed(!sidebarCollapsed)}
      />
      <main className={`App-main ${sidebarCollapsed ? 'sidebar-collapsed' : ''}`}>
        {renderPage()}
      </main>
    </div>
  )
}

export default App
