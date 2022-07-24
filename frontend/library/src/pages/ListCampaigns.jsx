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
            <h1> Listing all Campaigns </h1>  {
                items.map((item) => (
                <ol key = { item.id } >
                    CAMPAIGN_ID: { item.id },
                    CAMPAIGN_NAME: { item.name },
                    CAMPAIGN_SLOGAN: { item.slogan },
                    PARTNER_ID: { item.id }
                    </ol>
                ))
            }
        </div>
    );
}
}

export default ListCampaigns;