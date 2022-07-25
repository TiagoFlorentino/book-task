import React,  { useState } from "react";
import '../App.css';

function AddCampaign() {
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
        body: JSON.stringify({ name: inputs.name, slogan: inputs.slogan, partner_id: inputs.partner_id })
    };
    fetch('http://127.0.0.1:8000/add_campaign', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "AddCampaign">
     <h1> Add a new campaign to the library </h1>
     <form onSubmit={handleSubmit}>
      <fieldset>
      <p>Enter the name of the campaign:</p>
      <input
        type="text"
        name="name"
        value={inputs.name}
        onChange={handleChange}
      />
      <p>Enter the slogan of the campaign:</p>
      <input
        type="text"
        name="slogan"
        value={inputs.slogan}
        onChange={handleChange}
      />
      <p>Enter the ID partner of the campaign:</p>
      <input
        type="number"
        name="partner_id"
        value={inputs.partner_id}
        onChange={handleChange}
      />
       </fieldset>
     <input type="submit" />
    </form>
    </div>

  )
}

export default AddCampaign;