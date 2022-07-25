import React from "react";
import '../App.css';
class ListClients extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            items: [],
            DataisLoaded: false
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/list_clients")
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
        <div className = "ListClients">
        <h1> List clients of the library </h1>
        <table>
        <tr>
          <th>Client ID</th>
          <th>Client Status</th>
          <th>Created Date</th>
          <th>Status</th>
        </tr>
        {items.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.id}</td>
              <td>{val.name}</td>
              <td>{val.created}</td>
              <td>{((val.active === 1) ? 'Active' : 'Not Active')}</td>
            </tr>
          )
            })}
        </table>
        </div>
    );
}
}

export default ListClients;