import { React } from "react"
import { Box, Typography, Grid } from "@mui/material"

export default function TopHeader(title, v1, v2, v3, v4, v5) {
    const textStyle = {
      transform: 'rotate(90deg)',
    };

  return (
    <Grid item xs={3} sx={{backgroundColor:'red', height:'25%', border: '1px solid black'}}>
      <Box sx={{width:'100%', height:'100%'}}>
        
        <Box sx={{width:'100%', height:'25%', backgroundColor:'orange'}}>
          <Typography textAlign='center'>
            {title}
          </Typography>
        </Box>

        <Grid container xs={12} sx={{height:'75%'}}>
          
          <Grid item xs={12/5} marginTop='10px'>
            <Typography textAlign='right' style={textStyle}>
              {v1}
            </Typography>
          </Grid>

          <Grid item xs={12/5} marginTop='10px'>
            <Typography textAlign='right' style={textStyle}>
              {v2}
            </Typography>
          </Grid>

          <Grid item xs={12/5} marginTop='10px'>
            <Typography textAlign='right' style={textStyle}>
              {v3}
            </Typography>
          </Grid>

          <Grid item xs={12/5} marginTop='10px'>
            <Typography textAlign='right' style={textStyle}>
              {v4}
            </Typography>
          </Grid>

          <Grid item xs={12/5} marginTop='10px'>
            <Typography textAlign='right' style={textStyle}>
              {v5}
            </Typography>
          </Grid>
        </Grid>

      </Box>
    </Grid>
  );
}