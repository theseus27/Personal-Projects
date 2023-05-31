import React from 'react';
import '../Master.scss';
import './Header.scss';
import { Grid, Box } from "@mui/material";

function Header() {
  return (
    <>
      <Box className='containerBordersSide' sx={{ width: 1, flexDirection: 'column'}}>
        <Grid container xs={12}>
          <Grid item xs={4}>
            <p id="left">Header</p>
          </Grid>
          <Grid item xs={4}></Grid>
          <Grid item xs={4}>
            <p className="pagelink">Home</p>
            <p className="pagelink">About</p>
          </Grid>
        </Grid>
      </Box>
    </>
  )
}

export default Header;