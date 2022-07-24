import React,  { useState } from "react";
import {useLocation} from 'react-router-dom';

function ListCampaignLogs() {
    const location = useLocation();
      return (
        <div className = "ListCampaignLogs">
            <h1> List the campaign logs </h1>  {
                    location.state.map((item) => (
                    <ol key = { item.id } >
                        CAMPAIGN_ID: { item.campaign_id },
                        CLIENT_ID: { item.client_id },
                        NEW_CLIENT: {  (item.new_client === 1) ? "True" : "False" },
                        </ol>
                    ))
                }
        </div>
      );
    };

export default ListCampaignLogs;