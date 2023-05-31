import { React } from "react"
import { Grid } from "@mui/material"
import Clues from "./components/Clues"
import PuzzleGrid from "./components/PuzzleGrid"

export default function Homepage() {
  return (
  <>

  <div class="wrapper" id="home-page-wrapper" style={{backgroundColor:"black", height:'100%'}}>
      <Grid container sx={{height:'100%'}}>

        {/* {Spacer(5)}

        <Grid item xs={12} sx={{backgroundColor:'red'}}>
          <Typography textAlign="center" color="common.white">
              Title
          </Typography>
        </Grid>

        {Spacer(2)} */}

        {Clues()}

        {PuzzleGrid()}

      </Grid>
  </div>
  </>
  )
}
