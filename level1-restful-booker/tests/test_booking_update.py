def test_update_booking_put(booking):
    # Arrange
    client = booking["client"]
    booking_id = booking["booking_id"]
    updated_data = {
        "firstname": "UpdatedAyesha",
        "lastname": "Tester",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-15"
        },
        "additionalneeds": "Lunch"
    }
    # Act
    response = client.put(
        f"/booking/{booking_id}",
        json=updated_data
    )
    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "UpdatedAyesha"
    assert response_data["totalprice"] == 2000
def test_update_booking_patch(booking):
    # Arrange
    client = booking["client"]
    booking_id = booking["booking_id"]
    # Act
    response = client.patch(
        f"/booking/{booking_id}",
        json={
            "firstname": "PatchedAyesha"
        }
    )
    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "PatchedAyesha"
    # Verify other existing details remain unchanged
    assert response_data["lastname"] == "Tester"
    assert response_data["totalprice"] == 1500