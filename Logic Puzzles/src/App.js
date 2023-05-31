import Homepage from './Homepage';
import './App.css';

function App() {
  return (
    <>
      <header class="App-header">
        <p>
          Logic Puzzle Template
        </p>
      </header>
      <div class="wrapper" id="app-wrapper" style={{backgroundColor:"red"}}>
        <Homepage/>
      </div>
    </>
  );
}

export default App;
