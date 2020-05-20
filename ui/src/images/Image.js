import React from 'react'


function Image(props){
    return(
        <img 
        src={props.src} 
        alt={props.alt} 
        className={props.class}
        id={props.id}
        />
    )
}

export default Image;