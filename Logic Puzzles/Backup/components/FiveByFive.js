import { Tile } from './Tile';
import { FiveByFiveSX } from '../MUIstyle';
import { Box, Grid } from '@mui/material';

export function FiveByFive() {
  return (
    <>
    <Box sx={FiveByFiveSX}>
    <Grid container>
      {[...Array(5)].map((_, i) => (
        <Grid item key={i}>
          {[...Array(5)].map((_, j) => (
            Tile(`${i}, ${j}`)
          ))}
        </Grid>
      ))}
    </Grid>
    </Box>
    </>
  );
}