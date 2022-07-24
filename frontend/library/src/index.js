import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ListBooks from "./pages/ListBooks";
import ListClients from "./pages/ListClients";
import ListCampaigns from "./pages/ListCampaigns";
import ListPartners from "./pages/ListPartners";
import AddBook from "./pages/AddBook";


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/">
            <Route path="list_books" element={<ListBooks />} />
            <Route path="add_book" element={<AddBook />} />
            <Route path="list_clients" element={<ListClients />}/>
            <Route path="list_campaigns" element={<ListCampaigns />}/>
            <Route path="list_partners" element={<ListPartners />}/>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));