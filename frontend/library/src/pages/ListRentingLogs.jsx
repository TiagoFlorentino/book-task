import React from "react";
import {useLocation} from 'react-router-dom';

function ListRentingLogs() {
    const location = useLocation();
      return (
        <div className = "ListRentingLogs">
        <h1> List the renting logs </h1>
        <table>
        <tr>
          <th>Book ID</th>
          <th>Client ID</th>
          <th>Rented Date</th>
        </tr>
        {location.state.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.book_id}</td>
              <td>{val.client_id}</td>
              <td>{val.rented_date}</td>
            </tr>
          )
        })}
      </table>
       </div>
      );
    };

export default ListRentingLogs;