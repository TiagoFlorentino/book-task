import './App.css';
import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/navbar"
import ListBooks from "./pages/ListBooks";
import ListClients from "./pages/ListClients";
import ListCampaigns from "./pages/ListCampaigns";
import ListPartners from "./pages/ListPartners";
import AddBook from "./pages/AddBook";
import AddClient from "./pages/AddClient";
import AddPartner from "./pages/AddPartner";
import AddCampaign from "./pages/AddCampaign";
import RentBook from "./pages/RentBook";
import StatusClient from "./pages/StatusClient";
import StatusBook from "./pages/StatusBook";
import SearchBookLogs from "./pages/SearchBook";
import ListRentingLogs from "./pages/ListRentingLogs";
import ListCampaignLogs from "./pages/ListCampaignLogs";
import SearchCampaign from "./pages/SearchCampaign";
import SearchPartner from "./pages/SearchPartner";
import StatusPartner from "./pages/StatusPartner";
import ListPartnerLogs from "./pages/ListPartnerLogs";
import JoinCampaign from "./pages/JoinCampaign";
import Index from "./pages/Index";

export default function App() {
  return (
    <BrowserRouter>
     <Navbar />
      <Routes>
       <Route path="" element={<Index />} />
        <Route path="/">
            <Route path="list_books" element={<ListBooks />} />
            <Route path="add_book" element={<AddBook />} />
            <Route path="rent_book" element={<RentBook />} />
            <Route path="status_book" element={<StatusBook />} />
            <Route path="search_book" element={<SearchBookLogs />} />
            <Route path="renting_logs" element={<ListRentingLogs />} />

            <Route path="list_clients" element={<ListClients />}/>
            <Route path="add_client" element={<AddClient />} />
            <Route path="status_client" element={<StatusClient />} />

            <Route path="list_campaigns" element={<ListCampaigns />}/>
            <Route path="add_campaign" element={<AddCampaign />} />
            <Route path="search_campaign" element={<SearchCampaign />} />
            <Route path="campaign_logs" element={<ListCampaignLogs />} />
            <Route path="join_campaign" element={<JoinCampaign />} />

            <Route path="list_partners" element={<ListPartners />}/>
            <Route path="add_partner" element={<AddPartner />} />
            <Route path="status_partner" element={<StatusPartner />} />
            <Route path="search_partner" element={<SearchPartner />} />
            <Route path="partner_logs" element={<ListPartnerLogs />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));