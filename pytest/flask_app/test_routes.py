def test_request_example(client):
    response = client.get("/hello")
    assert "Hello, World!" in str(response.data)
