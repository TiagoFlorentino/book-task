import React,  { useState } from "react";
import '../App.css';
import { useNavigate } from 'react-router-dom';

function SearchPartnerLogs() {
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
    fetch('http://127.0.0.1:8000/partner_logs', requestOptions)
        .then(response => response.json())
        .then((json) => navigate('/partner_logs', {state: json}))
  }

  return (
  <div className = "SearchPartnerLogs">
     <h1> Search partner logs in the library </h1>
     <form onSubmit={handleSubmit}>
     <fieldset>
      <p>Enter the ID of the partner:</p>
      <input
        type="text"
        name="id"
        value={inputs.id}
        onChange={handleChange}
      />
    </fieldset>
    <input type="submit" />
    </form>
    </div>

  )
}

export default SearchPartnerLogs;