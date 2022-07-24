import React,  { useState } from "react";
import '../App.css';

function AddClient() {
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
        body: JSON.stringify({ name: inputs.name })
    };
    fetch('http://127.0.0.1:8000/add_client', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "AddClient">
     <h1> Add a new client to the library </h1>
         <form onSubmit={handleSubmit}>
      <label>Enter the name of the client:
      <input
        type="text"
        name="name"
        value={inputs.name}
        onChange={handleChange}
      />
      </label>
        <input type="submit" />
    </form>
    </div>

  )
}

export default AddClient;