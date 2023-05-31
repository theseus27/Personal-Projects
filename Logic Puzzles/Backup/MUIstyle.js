import { createTheme} from '@mui/material/styles';
const tileSize = "20px";

export const PuzzleTheme = createTheme({
    palette: {
      primary: {
        main: "#42a5f5"
      },
      secondary: {
        main: "#00ff00"
      },
    },
})

export const OuterBoxSX = {
  margin: '5% 10%',
  width: '80%',
  minHeight: 450,
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'center',
  alignContent: 'center',
  backgroundColor: 'primary.dark',
  // '&:hover': {
  //   backgroundColor: 'primary.main',
  //   opacity: [0.9, 0.8, 0.7],
  // },
}

export const TileSX = {
  backgroundColor: 'white',
  '&:hover': {
    backgroundColor: 'lightgray',
    opacity: [0.9, 0.8, 0.7],
  },
  width: tileSize,
  height: tileSize,
  border: '1px solid',
  borderColor: '#000000',
  flexGrow: 1,
}

export const FiveByFiveSX = {
  width: tileSize*5,
  height: tileSize*5,
  // width: "100px",
  // height: "100px",
  alignSelf: "center",
  border: '2px solid',
  borderColor: '#000000'
}

export const BreakSX = {
  width: "100%",
  margin: "2% 0% 0% 0%"
}