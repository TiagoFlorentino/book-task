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
            <h1> Listing all Partners </h1>  {
                items.map((item) => (
                <ol key = { item.id } >
                    PARTNER_ID: { item.id },
                    PARTNER_NAME: { item.name },
                    PARTNER_EMAIL: { item.email },
                    Status: { ((item.active === 1) ? 'Active' : 'Not Active')},
                    LAST_STATUS_UPDATE: { item.last_update },
                    </ol>
                ))
            }
        </div>
    );
}
}

export default ListPartners;