import { Tile } from './Tile';
import { Box, Grid } from '@mui/material';

export default function FiveByFive() {
  return (
      <Grid item xs={3} sx={{backgroundColor:'blue', height:'25%', border: '1px solid black'}}>
      <Grid container sx={{height:'100%'}}>
        {[...Array(5)].map((_, i) => (
          <>
          <Grid item key={i} xs={12/5} sx={{height:'19%'}}>
            {[...Array(5)].map((_, j) => (
              Tile(`${i}, ${j}`)
            ))}
          </Grid>
          </>
        ))}
      </Grid>
      </Grid>
  );
}