import React from 'react';
import ReactDOM from "react-dom"
import './index.css';
import App from './App'
import reportWebVitals from './reportWebVitals';
import { query_function } from './utils/query_function';
import { QueryClient, QueryClientProvider } from 'react-query';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      queryFn: query_function,
    },
  },
});

ReactDOM.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>,
  document.getElementById("root")
)

/*
const container = document.getElementById("root")
const root = ReactDOMClient.createRoot(container)

root.render (
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>
);
*/
reportWebVitals();
