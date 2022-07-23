import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ListBooks from "./pages/ListBooks";
import ListClients from "./pages/ListClients";



export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/">
            <Route path="list_books" element={<ListBooks />} />
            <Route path="list_clients" element={<ListClients />}/>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));