from utils.test_data import create_booking_data
def test_booking_data_builder():
    booking = create_booking_data()
    assert booking["firstname"] == "Ayesha"
    assert booking["lastname"] == "Tester"
    assert booking["totalprice"] == 1500
    assert booking["depositpaid"] is True
    assert booking["bookingdates"]["checkin"] == "2026-12-01"