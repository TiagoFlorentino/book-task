import React from "react";
import {useLocation} from 'react-router-dom';

function ListPartnerLogs() {
    const location = useLocation();
      return (
        <div className = "ListPartnerLogs">
        <h1> List the partner logs </h1>
        <table>
        <tr>
          <th>Partner ID</th>
          <th>Update date</th>
          <th>Active</th>
        </tr>
        {location.state.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.partner_id}</td>
              <td>{val.update_date}</td>
              <td>{(val.active === 1) ? "True" : "False"}</td>
            </tr>
          )
        })}
      </table>
        </div>
      );
    };

export default ListPartnerLogs;