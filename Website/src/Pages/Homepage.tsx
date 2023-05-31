import React from 'react';
import './Homepage.scss';
import Header from '../Components/Header'
import { Box, Typography } from "@mui/material"
import boxTheme from "./BoxTheme"

function Homepage() {
  return (
  <>

{ /* BEGIN HEADER */ }
    <div id="header">
      <Header />
    </div>
{ /* END HEADER */ }
    <Box sx={{ bgcolor:'purple' }}>
{ /* BEGIN BODY */ }
    <div className="body">
      <p>Hello!</p>
    </div>
{ /* END BODY */ }
    </Box>


    <Box sx={{boxTheme}}>
      <div className="body2">
        <Typography>
          Sup
        </Typography>
      </div>
    </Box>

  </>
  )
}

export default Homepage;