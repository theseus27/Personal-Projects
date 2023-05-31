import { React } from "react"
import { useState } from "react"
import { TileSX } from '../MUIstyle.js';
import { Box } from '@mui/material';
import  X from '../x.png';
import Check from '../checkmark.png';

export function Tile(coordinates) {
  const [status, setStatus] = useState(0);
  
  const changeStatus = () => {
    if (status === 0) { setStatus(1)}
    else if (status === 1) {setStatus(2)}
    else {setStatus(0)}
  }

  return (
    <>
    <Box sx={TileSX} value={status} onClick={changeStatus}>
      {status === 1 && 
        <img src={X} alt="x" width="20px" height="20px"/>
      }
      {status === 2 && 
        <img src={Check} alt="x" width="20px" height="20px"/>
      }
    </Box>
    </>
  );
}