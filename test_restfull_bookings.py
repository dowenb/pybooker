# test_restfull_bookings.py
import restfullbooker
from assertpy import assert_that

def test_bookings_for_mark():
    resp = restfullbooker.get_bookings('Mark')
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    for booking in resp.json():
        assert_that(resp.ok, 'HTTP Request OK').is_true()
        resp2 = restfullbooker.describe_booking(booking['bookingid'])
        assert_that(resp2.json()["firstname"], 'Firstname').contains('Mark')

def test_addbooking():
    resp = restfullbooker.add_booking()
    print(resp.json())
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    #TODO construct a booking to create and assert created booking against it

def test_updatebooking():
        auth_token = restfullbooker.get_authtoken().json()['token']
        marks_booking = restfullbooker.get_bookings('Mark').json()[0]['bookingid']
        resp = restfullbooker.update_booking(marks_booking, auth_token)
        assert_that(resp.ok)