import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import { Des } from './Components/Des'
import { Nav } from './Components/Nav'
import { Foot } from './Components/Foot'

function App() {
  return (
    <>
    <Nav/>
    <Des/>
    <Foot/>
    </>
  )
}

export default App
