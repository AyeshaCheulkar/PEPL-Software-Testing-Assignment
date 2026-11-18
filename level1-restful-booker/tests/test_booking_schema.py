import json
from pathlib import Path
from jsonschema import validate
from utils.api_client import APIClient
from utils.test_data import create_booking_data
def test_booking_response_schema():
    # Arrange
    client = APIClient()
    booking_data = create_booking_data()
    # Act
    response = client.post(
        "/booking",
        json=booking_data
    )
    assert response.status_code == 200
    response_data = response.json()
    # Load expected JSON schema
    schema_path = (
        Path(__file__).parent.parent
        / "schemas"
        / "booking_schema.json"
    )
    with open(schema_path, "r", encoding="utf-8") as file:
        booking_schema = json.load(file)
    # Validate response structure
    validate(
        instance=response_data["booking"],
        schema=booking_schema
    )
