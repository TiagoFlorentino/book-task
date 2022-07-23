# Endpoints


## Campaign Operations

### GET - /list_campaigns

Description: list all the campaigns of the library

### POST - /add_campaign

Description: Add a new campaign to the library

```json
{
  "name": "Campaign A",
  "slogan": "Reading, Good!",
  "partner_id": 1
}
```

### POST - /join_campaign

Description: A client can join a campaign

```json
{
  "client_id": 1,
  "campaign_id": 1
}
```

## Campaign Logs Operations

### GET - /list_campaign_logs

Description: list all the campaign logs of the library