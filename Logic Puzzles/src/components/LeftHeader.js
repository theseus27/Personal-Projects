import React from 'react';
import TopHeader from './TopHeader';
import { Box } from '@mui/material';

const rotatedStyle = {
  transform: 'rotate(180deg)',
};

export default function LeftHeader() {
  return (
    <Box style={rotatedStyle}>
      <TopHeader/>
    </Box>
  )
}

// import { React } from "react"
// import { Box, Typography, Grid } from "@mui/material"

// export default function LeftHeader(title, v1, v2, v3, v4, v5) {
//   const textStyle = {
//     transform: 'rotate(270deg)',
//   };

//   return (
//     <Grid item xs={3} sx={{backgroundColor:'green', height:'25%', border: '1px solid black', flexDirection:'column'}}>
//       <Box sx={{width:'100%', height:'100%'}}>
        
//         <Box sx={{width:'25%', height:'100%', backgroundColor:'orange'}}>
//           <Typography textAlign='left' style={textStyle} sx={{paddingTop:'20px', paddingRight:'12px'}}>
//             {title}
//           </Typography>
//         </Box>

//         <Grid container sx={{height:'100%', width:'75%', marginLeft:'25%'}}>
//           <Grid item xs={12} sx={{height:'20%'}}>
//               <Typography backgroundColor='pink'>
//                 {v1}
//               </Typography>
//           </Grid>
//         </Grid>

//       </Box>
//     </Grid>
//   );
// }