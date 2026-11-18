from utils.api_client import APIClient
from utils.test_data import create_booking_data
def test_create_booking():
    # Arrange
    client = APIClient()
    booking_data = create_booking_data()
    # Act
    response = client.post(
        "/booking",
        json=booking_data
    )
    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert "bookingid" in response_data
    assert "booking" in response_data
    assert response_data["booking"]["firstname"] == "Ayesha"
    assert response_data["booking"]["lastname"] == "Tester"