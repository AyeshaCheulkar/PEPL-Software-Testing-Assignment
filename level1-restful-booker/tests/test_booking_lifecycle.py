
from utils.api_client import APIClient
from utils.test_data import create_booking_data


def test_complete_booking_lifecycle():
    # Step 1: Create API client
    client = APIClient()

    # Step 2: Authenticate and obtain token
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

    booking_id = None

    try:
        # Step 3: CREATE a booking
        booking_data = create_booking_data()

        create_response = client.post(
            "/booking",
            json=booking_data
        )

        assert create_response.status_code == 200

        booking_id = create_response.json()["bookingid"]
        assert booking_id is not None

        # Step 4: READ the created booking
        read_response = client.get(
            f"/booking/{booking_id}"
        )

        assert read_response.status_code == 200
        assert read_response.json()["firstname"] == booking_data["firstname"]

        # Step 5: UPDATE the complete booking using PUT
        updated_data = booking_data.copy()
        updated_data["firstname"] = "Updated"
        updated_data["totalprice"] = 2000

        put_response = client.put(
            f"/booking/{booking_id}",
            json=updated_data
        )

        assert put_response.status_code == 200
        assert put_response.json()["firstname"] == "Updated"
        assert put_response.json()["totalprice"] == 2000

        # Step 6: PARTIALLY UPDATE the booking using PATCH
        patch_response = client.patch(
            f"/booking/{booking_id}",
            json={"firstname": "Patched"}
        )

        assert patch_response.status_code == 200
        assert patch_response.json()["firstname"] == "Patched"
        assert patch_response.json()["totalprice"] == 2000

        # Step 7: DELETE the booking
        delete_response = client.delete(
            f"/booking/{booking_id}"
        )

        assert delete_response.status_code == 201

        # Step 8: VERIFY that the booking no longer exists
        final_response = client.get(
            f"/booking/{booking_id}"
        )

        assert final_response.status_code == 404

    finally:
        # Cleanup if the test fails before deletion
        if booking_id is not None:
            check_response = client.get(
                f"/booking/{booking_id}"
            )

            if check_response.status_code == 200:
                client.delete(
                    f"/booking/{booking_id}"
                )
