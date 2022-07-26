# Endpoints


## Partner Operations

### GET - /list_partners

Description: list all the partners of the library

### POST - /add_partner

Description: Add a new partner to the library

```json
{
  "name": "Mahna Mahna",
  "slogan": "mahna_mahna@xyz.com",
}
```

### POST - /partner_status

Description: A partner can change it's status

```json
{
  "id": 1,
  "active": true // or false
}
```

### GET - /list_partner_logs

Description: list all the partner_logs of the library