import React,  { useState } from "react";

import '../App.css';

function JoinCampaign() {
  const [inputs, setInputs] = useState({});

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
        body: JSON.stringify({ campaign_id: inputs.campaign_id, client_id:inputs.client_id })
    };
    fetch('http://127.0.0.1:8000/join_campaign', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "JoinCampaign">
     <h1> Join a campaign! </h1>
     <form onSubmit={handleSubmit}>
     <fieldset>
      <p>Enter the client ID:</p>
      <input
        type="number"
        name="client_id"
        value={inputs.client_id}
        onChange={handleChange}
      />
      <p>Enter the campaign ID:</p>
      <input
        type="number"
        name="campaign_id"
        value={inputs.campaign_id}
        onChange={handleChange}
      />
      </fieldset>
    <input type="submit" />
    </form>
    </div>

  )
}

export default JoinCampaign;