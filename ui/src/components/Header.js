import React from 'react'
import './Main.css'
import Image from '../images/Image'
import {LOGOPNG} from '../images/ImageIndex'


function Header()
{
    return(
    <header>
      <Image src={LOGOPNG} alt='logo missing' id='logo' />
      <h1>PLKN</h1>
    </header>);
}

export default Header;