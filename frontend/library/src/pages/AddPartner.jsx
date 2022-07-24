import React,  { useState } from "react";
import '../App.css';

function AddPartner() {
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
        body: JSON.stringify({ name: inputs.name, email: inputs.email })
    };
    fetch('http://127.0.0.1:8000/add_partner', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "AddClient">
     <h1> Add a new partner to the library </h1>
     <form onSubmit={handleSubmit}>
      <li>
      <label>Enter the name of the partner:
      <input
        type="text"
        name="name"
        value={inputs.name}
        onChange={handleChange}
      />
      </label>
      </li>
      <li>
      <label>Enter the email of the partner:
      <input
        type="text"
        name="email"
        value={inputs.email}
        onChange={handleChange}
      />
      </label>
    </li>
      <input type="submit" />
    </form>
    </div>

  )
}

export default AddPartner;