import React,  { useState } from "react";
import '../App.css';
import { useNavigate } from 'react-router-dom';

function SearchCampaign() {
  const [inputs, setInputs] = useState({});
  const navigate = useNavigate();


  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: inputs.id })
    };
    fetch('http://127.0.0.1:8000/campaign_logs', requestOptions)
        .then(response => response.json())
        .then((json) => navigate('/campaign_logs', {state: json}))
  }

  return (
  <div className = "SearchCampaign">
     <h1> Search campaign logs in the library </h1>
         <form onSubmit={handleSubmit}>
      <li>
      <label>Enter the ID of the campaign:
      <input
        type="number"
        name="id"
        value={inputs.id}
        onChange={handleChange}
      />
      </label>
    </li>
    <input type="submit" />
    </form>
    </div>

  )
}

export default SearchCampaign;