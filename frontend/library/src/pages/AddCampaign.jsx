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
  <div className = "AddBook">
     <h1> Add a new campaign to the library </h1>
         <form onSubmit={handleSubmit}>
         <li>
      <label>Enter the name of the book:
      <input
        type="text"
        name="name"
        value={inputs.name}
        onChange={handleChange}
      />
      </label>
      </li>
      <li>
      <label>Enter the slogan of the campaign:
      <input
        type="text"
        name="slogan"
        value={inputs.slogan}
        onChange={handleChange}
      />
      </label>
      </li>
      <li>
      <label>Enter the ID partner of the campaign:
      <input
        type="number"
        name="partner_id"
        value={inputs.partner_id}
        onChange={handleChange}
      />
      </label>
      </li>
     <input type="submit" />
    </form>
    </div>

  )
}

export default AddCampaign;