import { React } from "react"
import { Box, Typography } from '@mui/material';

export function Tile( coordinates ) {

  return (
      <Box sx={{height:'100%', width:'100%', alignContent:'center', justifyContent:'center', border: '1px solid black'}}>
        <Typography fontSize='8px'>
          {coordinates}
        </Typography>
      </Box>
  );
}