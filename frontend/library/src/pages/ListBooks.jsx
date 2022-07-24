import React from "react";
import '../App.css';
class ListBooks extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            items: [],
            DataisLoaded: false
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/list_books")
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
        <div className = "ListBooks">
            <h1> Listing all books </h1>  {
                items.map((item) => (
                <ol key = { item.id } >
                    BOOK_ID: { item.id },
                    BOOK_TITLE: { item.title },
                    BOOK_STATUS: { item.status }
                    LAST_RENTER_ID: { item.renter_id }
                    </ol>
                ))
            }
        </div>
    );
}
}

export default ListBooks;