import React from "react";
import {useLocation} from 'react-router-dom';

function ListCampaignLogs() {
    const location = useLocation();
      return (
        <div className = "ListCampaignLogs">
                <h1> List campaigns logs </h1>
        <table>
        <tr>
          <th>Campaign ID</th>
          <th>Client ID</th>
          <th>New Client</th>
        </tr>
        {location.state.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.campaign_id}</td>
              <td>{val.client_id}</td>
              <td>{ (val.new_client === 1) ? "True" : "False"}</td>
            </tr>
          )
            })}
        </table>
        </div>
      );
    };

export default ListCampaignLogs;