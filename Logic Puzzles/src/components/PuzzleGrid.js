import { React } from "react"
import { Box, Typography, Grid } from "@mui/material"
import Spacer from './Spacer';
import TopHeader from './TopHeader';
import LeftHeader from './LeftHeader';
import FiveByFive from './FiveByFive';

export default function PuzzleGrid() {
  return (
    <Box id="right" xs={6} sx={{backgroundColor:'brown', justifyItems:'center', marginLeft: '5%', marginRight: '5%', marginTop:'2%', width:'65%', height:'80%'}}>

    <Grid container xs={12} sx={{backgroundColor:'black', width:"100%", height:"100%"}}>
    {/* Row 1 */}
        <Grid item xs={3} sx={{backgroundColor:'white', height:'25%', border: '1px solid black'}}></Grid>
        {TopHeader("Title 1", "Var1", "Var2", "Var3", "Var4", "Var 5")}
        {TopHeader("Title 2", "Var1", "Var2", "Var3", "Var4", "Var 5")}
        {TopHeader("Title 3", "Var1", "Var2", "Var3", "Var4", "Var 5")}
        

      {/* Row 2 */}
        {LeftHeader("Title 4", "Var1", "Var2", "Var3", "Var4", "Var 5")}
        {FiveByFive()}
        {FiveByFive()}
        {FiveByFive()}

      {/* Row 3 */}
      {LeftHeader("Title 3", "Var1", "Var2", "Var3", "Var4", "Var 5")}
      {FiveByFive()}
      {FiveByFive()}
      <Grid item xs={3} sx={{backgroundColor:'white', height:'25%', border: '1px solid black'}}></Grid>

      {/* Row 4 */}
      {LeftHeader("Title 2", "Var1", "Var2", "Var3", "Var4", "Var 5")}
      {FiveByFive()}
      <Grid item xs={3} sx={{backgroundColor:'white', height:'25%', border: '1px solid black'}}></Grid>
      <Grid item xs={3} sx={{backgroundColor:'white', height:'25%', border: '1px solid black'}}></Grid>
      </Grid>
      
      {/* <Grid item xs={12}>
        {FiveByFive()}
      </Grid> */}
    </Box>
  );
}