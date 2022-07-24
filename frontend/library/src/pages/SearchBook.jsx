import React,  { useState } from "react";
import '../App.css';
import { useNavigate } from 'react-router-dom';

function SearchBookLogs() {
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
        body: JSON.stringify({ book_id: inputs.book_id })
    };
    fetch('http://127.0.0.1:8000/book_renting_logs', requestOptions)
        .then(response => response.json())
        .then((json) => navigate('/renting_logs', {state: json}))
  }

  return (
  <div className = "SearchBookLogs">
     <h1> Search book logs in the library </h1>
         <form onSubmit={handleSubmit}>
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

export default SearchBookLogs;