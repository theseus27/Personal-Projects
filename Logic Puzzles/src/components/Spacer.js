import React from 'react'
import { Grid } from "@mui/material"

function Spacer( goalHeight ) {
  return (
    <Grid item xs={12} 
      sx={{
        margin: goalHeight + 'px'
      }}
    />
  )
}

export default Spacer
