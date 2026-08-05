from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hello from Docker v2!"
    }


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data.decode() == "OK"


def test_whoami():
    client = app.test_client()

    response = client.get("/whoami")

    assert response.status_code == 200

    data = response.get_json()

    assert "hostname" in data
