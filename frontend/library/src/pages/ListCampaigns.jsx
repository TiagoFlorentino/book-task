import React from "react";
import '../App.css';
class ListCampaigns extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            items: [],
            DataisLoaded: false
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/list_campaigns")
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
        <div className = "ListCampaigns">
        <h1> List campaigns of the library </h1>
        <table>
        <tr>
          <th>Campaign ID</th>
          <th>Campaign Name</th>
          <th>Campaign Slogan</th>
          <th>Partner ID</th>
        </tr>
        {items.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.id}</td>
              <td>{val.name}</td>
              <td>{val.slogan}</td>
              <td>{val.partner_id}</td>
            </tr>
          )
            })}
        </table>
        </div>
    );
}
}

export default ListCampaigns;