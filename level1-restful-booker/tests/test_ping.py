from utils.api_client import APIClient
def test_ping():
    # Arrange
    client = APIClient()
    # Act
    response = client.get("/ping")
    # Assert
    assert response.status_code == 201