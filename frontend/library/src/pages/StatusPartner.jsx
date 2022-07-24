import React,  { useState } from "react";
import '../App.css';

function StatusPartner() {
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
        body: JSON.stringify({ id: inputs.id, active: (inputs.active === "true") ? true : false })
    };
    fetch('http://127.0.0.1:8000/partner_status', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "StatusPartner">
     <h1> Change the status of a partner on the library </h1>
     <form onSubmit={handleSubmit}>
      <li>
      <label>Enter the ID of the partner:
      <input
        type="text"
        name="id"
        value={inputs.id}
        onChange={handleChange}
      />
      </label>
      </li>
      <li>
      <label>Enter the active status of the partner (true/false):
      <input
        type="text"
        name="active"
        value={inputs.active}
        onChange={handleChange}
      />
      </label>
    </li>
      <input type="submit" />
    </form>
    </div>

  )
}

export default StatusPartner;