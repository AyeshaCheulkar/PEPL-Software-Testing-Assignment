def test_delete_booking(booking):
    # Arrange
    client = booking["client"]
    booking_id = booking["booking_id"]
    # Act: Delete booking
    delete_response = client.delete(
        f"/booking/{booking_id}"
    )
    # Assert: Verify deletion response
    assert delete_response.status_code == 201
    # Verify that deleted booking cannot be retrieved
    get_response = client.get(
        f"/booking/{booking_id}"
    )
    assert get_response.status_code == 404