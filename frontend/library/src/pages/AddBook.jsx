import React,  { useState } from "react";
import '../App.css';

function AddBook() {
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
        body: JSON.stringify({ title: inputs.title })
    };
    fetch('http://127.0.0.1:8000/add_book', requestOptions)
        .then(response => response.json())
        .then((json) => alert("Request Completed"))
  }

  return (
  <div className = "AddBook">
     <h1> Add a new book to the library </h1>
         <form onSubmit={handleSubmit}>
      <li>
      <label>Enter the title of the book:
      <input
        type="text"
        name="title"
        value={inputs.title}
        onChange={handleChange}
      />
      </label>
    </li>
    <input type="submit" />
    </form>
    </div>

  )
}

export default AddBook;