import { React } from "react"
import { PuzzleTheme, OuterBoxSX, BreakSX} from '../MUIstyle'
import { Box, Typography, Grid } from "@mui/material"
import { ThemeProvider } from "@mui/material/styles"
import { FiveByFive } from './FiveByFive'

export default function PuzzleGrid() {
  //0 = clear, 1 = check, 2 = x
  
  return (<> <ThemeProvider theme={PuzzleTheme}>
  <Box sx={OuterBoxSX}>
    <Grid container>
      <Grid item xs={12}>
        <Typography textAlign="center" color="common.white">
            Options
        </Typography>
      </Grid>
      {/* <Box sx={BreakSX}/> */}
      <Grid item width="120px" height="120px">
        {FiveByFive()}
      </Grid>
    </Grid>
  </Box>

  {/* <Box sx={OuterBoxSX}>

      <Typography textAlign="center" color="common.white">
        Options
      </Typography>

      <Box sx={BreakSX}/>

        {FiveByFive()}
        {FiveByFive()}
        {FiveByFive()}
      
  </Box> */}

  </ThemeProvider></>);
}
