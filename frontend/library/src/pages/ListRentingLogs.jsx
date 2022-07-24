import React,  { useState } from "react";
import {useLocation} from 'react-router-dom';

function ListRentingLogs() {
    const location = useLocation();
      return (
        <div className = "ListRentingLogs">
            <h1> List the renting logs </h1>  {
                    location.state.map((item) => (
                    <ol key = { item.id } >
                        BOOK_ID: { item.book_id },
                        CLIENT_ID: { item.client_id },
                        RENTED_DATE: { item.rented_date },
                        </ol>
                    ))
                }
        </div>
      );
    };

export default ListRentingLogs;