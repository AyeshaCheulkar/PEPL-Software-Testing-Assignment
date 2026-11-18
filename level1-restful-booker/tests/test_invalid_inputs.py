import pytest
from utils.api_client import APIClient
@pytest.mark.parametrize(
    "booking_id, expected_status",
    [
        (0, 404),
        (-1, 404),
        (999999, 404),
        ("not-a-number", 404),
    ]
)
def test_invalid_booking_ids(booking_id, expected_status):
    # Arrange
    client = APIClient()
    # Act
    response = client.get(
        f"/booking/{booking_id}"
    )
    # Assert
    assert response.status_code == expected_status