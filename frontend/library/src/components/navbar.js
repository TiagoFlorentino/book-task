import React from 'react';
import {
  Nav,
  NavLink,
  NavMenu,
} from './NavBarElement.js';

const Navbar = () => {
  return (
    <>
      <Nav>
        <NavMenu>
          <NavLink to='/add_book' activeStyle>
            Add Book
          </NavLink>
         <NavLink to='/add_client' activeStyle>
            Add Client
          </NavLink>
         <NavLink to='/add_partner' activeStyle>
            Add Partner
          </NavLink>
         <NavLink to='/add_campaign' activeStyle>
            Add Campaign
          </NavLink>
          <NavLink to='/list_books' activeStyle>
            List Book
          </NavLink>
         <NavLink to='/list_clients' activeStyle>
            List Clients
          </NavLink>
          <NavLink to='/list_partners' activeStyle>
            List Partners
          </NavLink>
         <NavLink to='/list_campaigns' activeStyle>
            List Campaigns
          </NavLink>
          <NavLink to='/rent_book' activeStyle>
            Rent Book
          </NavLink>
         <NavLink to='/search_book' activeStyle>
            Search Book
          </NavLink>
          <NavLink to='/search_partner' activeStyle>
            Search Partner
          </NavLink>
         <NavLink to='/search_campaign' activeStyle>
            Search Campaign
          </NavLink>
         <NavLink to='/status_book' activeStyle>
            Status Book
          </NavLink>
          <NavLink to='/status_client' activeStyle>
            Status Client
          </NavLink>
         <NavLink to='/status_partner' activeStyle>
            Status Partner
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default Navbar;