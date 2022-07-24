import React,  { useState } from "react";
import '../App.css';

function RentBook() {
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
        body: JSON.stringify({ book_id: inputs.book_id, client_id: inputs.client_id })
    };
    fetch('http://127.0.0.1:8000/rent_book', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "RentBook">
     <h1> Rent a book in the library </h1>
         <form onSubmit={handleSubmit}>
      <li>
      <label>Enter the ID of the client:
      <input
        type="text"
        name="client_id"
        value={inputs.client_id}
        onChange={handleChange}
      />
      </label>
    </li>
      <li>
      <label>Enter the ID of the book:
      <input
        type="text"
        name="book_id"
        value={inputs.book_id}
        onChange={handleChange}
      />
      </label>
    </li>
    <input type="submit" />
    </form>
    </div>

  )
}

export default RentBook;