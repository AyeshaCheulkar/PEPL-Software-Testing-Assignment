def test_read_booking(booking):
    # Arrange
    client = booking["client"]
    booking_id = booking["booking_id"]
    # Act
    response = client.get(
        f"/booking/{booking_id}"
    )
    # Assert
    assert response.status_code == 200
    booking_details = response.json()
    assert booking_details["firstname"] == "Ayesha"
    assert booking_details["lastname"] == "Tester"
    assert booking_details["totalprice"] == 1500
    assert booking_details["depositpaid"] is True
    assert "bookingdates" in booking_details