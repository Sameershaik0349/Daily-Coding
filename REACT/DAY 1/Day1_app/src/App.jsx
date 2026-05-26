import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

import { Home } from './Components/Home'
// import { Count } from './Components/Count'
import { Nav } from  './Components/Nav'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Nav/>
      <Home/>
      {/* <Count/> */}
    </>
  )
}

export default App
