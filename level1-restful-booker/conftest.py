import pytest
from utils.api_client import APIClient
from utils.test_data import create_booking_data
@pytest.fixture
def booking():
    # Create API client
    client = APIClient()
    # Authenticate
    auth_response = client.post(
        "/auth",
        json={
            "username": "admin",
            "password": "password123"
        }
    )
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]
    client.session.cookies.set("token", token)
    # Create a new booking
    booking_data = create_booking_data()
    create_response = client.post(
        "/booking",
        json=booking_data
    )
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]
    # Provide booking details to the test
    yield {
        "client": client,
        "booking_id": booking_id
    }
    # Cleanup: Delete the booking after the test
    check_response = client.get(
        f"/booking/{booking_id}"
    )
    if check_response.status_code == 200:
        client.delete(
            f"/booking/{booking_id}"
        )