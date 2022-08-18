import React from "react";

import AppBar from "@mui/material/AppBar";
import { Link } from "react-router-dom";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";

const Page = ({ title, children }) => {
  return (
    <Box paddingX={3} paddingTop={12}>
      <AppBar>
        <Toolbar>
          <Link to="/">
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
            >
            </IconButton>
          </Link>
          <Typography variant="h6" component="div">
            Pokemon: {title}
          </Typography>
        </Toolbar>
      </AppBar>
      {children}
    </Box>
  );
};
export default Page;