import React,  { useState } from "react";
import '../App.css';

function StatusBook() {
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
        body: JSON.stringify({ id: inputs.id, status: inputs.status })
    };
    fetch('http://127.0.0.1:8000/book_status', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "StatusBook">
     <h1>  Changes status of a book in the library </h1>
     <form onSubmit={handleSubmit}>
      <fieldset>
      <p>Enter the ID of the book:</p>
      <input
        type="text"
        name="id"
        value={inputs.id}
        onChange={handleChange}
      />
      <p>Enter the active status of the book (AVAILABLE or DISCONTINUED):</p>
      <input
        type="text"
        name="status"
        value={inputs.status}
        onChange={handleChange}
      />
       </fieldset>
      <input type="submit" />
    </form>
    </div>

  )
}

export default StatusBook;