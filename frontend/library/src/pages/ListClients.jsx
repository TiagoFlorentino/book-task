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
            <h1> Listing all clients </h1>  {
                items.map((item) => (
                <ol key = { item.id } >
                    CLIENT_ID: { item.id },
                    CLIENT_STATUS: { item.name },
                    CLIENT_CREATE: { item.created },
                    CLIENT_ACTIVE_STATUS: { ((item.active === 1) ? 'Active' : 'Not Active')}
                    </ol>
                ))
            }
        </div>
    );
}
}

export default ListClients;