from utils.api_client import APIClient
def test_default_base_url():
    client = APIClient()
    assert client.base_url == "http://localhost:3001"
def test_custom_base_url():
    client = APIClient(
        base_url="http://example.com"
    )
    assert client.base_url == "http://example.com"
def test_environment_base_url(monkeypatch):
    monkeypatch.setenv(
        "BASE_URL",
        "http://localhost:3001"
    )
    client = APIClient()
    assert client.base_url == "http://localhost:3001"