def test_http_create_user(http_client):
    response = http_client.post("/", json={"name": "xiaoming", "phone": "12345678901"})
    assert response.status_code == 200


def test_http_read_user(http_client):
    response = http_client.get("/")
    assert response.status_code == 200
