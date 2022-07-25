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
        <h1> Listing all books in the library </h1>
        <table>
        <tr>
          <th>Book ID</th>
          <th>Title</th>
          <th>Status</th>
          <th>Current renter ID</th>
        </tr>
        {items.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.id}</td>
              <td>{val.title}</td>
              <td>{val.status}</td>
              <td>{val.renter_id}</td>
            </tr>
          )
            })}
        </table>
        </div>
    );
}
}

export default ListBooks;