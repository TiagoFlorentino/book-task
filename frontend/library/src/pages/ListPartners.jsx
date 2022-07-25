import React from "react";
import '../App.css';
class ListPartners extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            items: [],
            DataisLoaded: false
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/list_partners")
            .then((res) => res.json())
            .then((json) => {
                this.setState({
                    items: json,
                    DataisLoaded: true
                });
            })
    }
    render() {
        const { DataisLoaded, items } = this.state;
        if (!DataisLoaded) return <div>
            <h1> Please wait some time.... </h1> </div> ;

        return (
        <div className = "ListPartners">
        <h1> Partner List </h1>
        <table>
           <tr>
              <th>Partner ID</th>
              <th>Partner Name</th>
              <th>Partner Email</th>
              <th>Current Status</th>
              <th>Last Status Update</th>
            </tr>
            {items.map((val, key) => {
              return (
                <tr key={key}>
                  <td>{val.id}</td>
                  <td>{val.name}</td>
                  <td>{val.email}</td>
                  <td>{((val.active === 1) ? 'Active' : 'Not Active')}</td>
                  <td>{val.last_update}</td>
                </tr>
              )
            })}
          </table>
        </div>
    );
}
}

export default ListPartners;