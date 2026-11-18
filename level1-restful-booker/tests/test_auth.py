from utils.api_client import APIClient
def test_valid_authentication():
    # Arrange
    client = APIClient()
    credentials = {
        "username": "admin",
        "password": "password123"
    }
    # Act
    response = client.post(
        "/auth",
        json=credentials
    )
    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert "token" in response_data
    assert response_data["token"] is not None

def test_invalid_authentication():
    # Arrange
    client = APIClient()
    credentials = {
        "username": "wronguser",
        "password": "wrongpassword"
    }
    # Act
    response = client.post(
        "/auth",
        json=credentials
    )
    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert "reason" in response_data

from utils.test_data import create_booking_data
def test_token_cookie_authentication():
    client = APIClient()
    # Step 1: Login and obtain token
    credentials = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = client.post(
        "/auth",
        json=credentials
    )
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]
    assert token
    # Step 2: Create a booking
    booking_data = create_booking_data()
    booking_response = client.post(
        "/booking",
        json=booking_data
    )
    assert booking_response.status_code == 200
    booking_id = booking_response.json()["bookingid"]
    # Step 3: Update booking using token cookie
    client.session.cookies.set("token", token)
    updated_data = create_booking_data()
    updated_data["firstname"] = "TokenUser"
    update_response = client.put(
        f"/booking/{booking_id}",
        json=updated_data
    )
    # Step 4: Verify update
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == "TokenUser"
def test_basic_authentication():
    client = APIClient()
    # Step 1: Create a booking
    booking_data = create_booking_data()
    booking_response = client.post(
        "/booking",
        json=booking_data
    )
    assert booking_response.status_code == 200
    booking_id = booking_response.json()["bookingid"]
    # Step 2: Prepare updated booking data
    updated_data = create_booking_data()
    updated_data["firstname"] = "BasicUser"
    # Step 3: Update using Basic authentication
    update_response = client.put(
        f"/booking/{booking_id}",
        json=updated_data,
        auth=("admin", "password123")
    )
    # Step 4: Verify update
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == "BasicUser"