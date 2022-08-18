import axios from "axios";

import { QueryFunction } from "react-query"

export const query_function = async ({ queryKey }) => {
  const { data } = await axios.get(`http://localhost:8000/${queryKey[0]}`);
  var parsed = JSON.parse(data)
  return parsed;
}