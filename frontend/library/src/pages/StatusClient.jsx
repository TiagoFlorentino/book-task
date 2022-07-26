import React,  { useState } from "react";
import '../App.css';

function StatusClient() {
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
    fetch('http://127.0.0.1:8000/client_status', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "StatusClient">
     <h1> Change the status of a client on the library </h1>
     <form onSubmit={handleSubmit}>
     <fieldset>
      <p>Enter the ID of the client:</p>
      <input
        type="text"
        name="id"
        value={inputs.id}
        onChange={handleChange}
      />
      <p>Enter the active status of the client:</p>
        <select name="active" onChange={handleChange}>
           <option value="none" selected disabled hidden>Select an Option</option>
           <option value="true">true</option>
           <option value="false">false</option>
      </select>
    </fieldset>
      <input type="submit" />
    </form>
    </div>

  )
}

export default StatusClient;