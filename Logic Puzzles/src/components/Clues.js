import { React } from "react"
import { Box, Typography } from "@mui/material"

export default function Clues() {
  return (
    <Box id="left" sx={{backgroundColor:'grey', width:'15%', marginLeft:'5%', paddingLeft: '1%', paddingRight:'1%', height:'80%', marginTop:'2%'}}>
      <Typography textAlign="center" color="common.white">
          Title
      </Typography>
      <Typography textAlign="left" color="common.white">
        Clues
      </Typography>
    </Box>
  );
}