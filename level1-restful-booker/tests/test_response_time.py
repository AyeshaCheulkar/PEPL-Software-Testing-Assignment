import time
from utils.api_client import APIClient
def test_api_response_time():
    # Arrange
    client = APIClient()
    # Act
    start_time = time.perf_counter()
    response = client.get("/ping")
    end_time = time.perf_counter()
    response_time = end_time - start_time
    # Assert
    assert response.status_code == 201
    assert response_time < 2.0, (
        f"API response took {response_time:.3f} seconds"
    )
    print(
        f"\nAPI Response Time: {response_time:.4f} seconds"
    )
