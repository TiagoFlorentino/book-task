import React from "react";
import {useLocation} from 'react-router-dom';

function ListPartnerLogs() {
    const location = useLocation();
      return (
        <div className = "ListPartnerLogs">
            <h1> List the partner logs </h1>  {
                    location.state.map((item) => (
                    <ol key = { item.id } >
                        PARTNER_ID: { item.partner_id },
                        UPDATE_DATE: { item.update_date },
                        ACTIVE: {  (item.active === 1) ? "True" : "False" },
                        </ol>
                    ))
                }
        </div>
      );
    };

export default ListPartnerLogs;