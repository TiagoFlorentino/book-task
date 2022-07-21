# Endpoints

## Client Operations

### GET - /list_clients

Description: list the clients on the library

### POST - /search_client

Description: Search a client by name or ID

Examples:

- by ID
    ```json
    {
      "id": 1
    }
    ```

- by Name
    ```json
    {
      "name": "JOSE ANTONIO"
    }
    ```

### POST - /client_status

Description: Activate or Deactivate a client by ID

Examples:

```json
{
  "id": 1,
  "active": true // or false
}
```


### POST - /add_client

Description: Create a new client to the library

Example:

```json
{
  "name": "JOSE ANTONIO"
}
```