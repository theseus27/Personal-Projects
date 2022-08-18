import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ShowAll from './routes/Pokemon';
import ShowOne from "./routes/Pokemon/search";

import CssBaseline from "@mui/material/CssBaseline";

function App() {
  return (
    <div className="App">
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<ShowAll />}></Route>
          <Route path=":id/" element={<ShowOne />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;