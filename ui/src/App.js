import React from 'react';
import './App.css';
import Image from './images/Image'
import {LOGOPNG} from './images/ImageIndex'

function App() {
  return (
    <div className="App">
      <Image src={LOGOPNG} alt='puppy missing' id='logo' />
      <h1>PLKN</h1>


    </div>
  );
}

export default App;
