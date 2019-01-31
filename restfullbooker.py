# restfullbooker.py
import requests


def _url(path):
    return 'https://restful-booker.herokuapp.com' + path


def get_bookings(firstname="", lastname="", checkin="", checkout=""):
    payload = {}
    if firstname:
        payload['firstname'] = firstname
    if lastname:
        payload['lastname'] = lastname
    if checkin:
        payload['checkin'] = checkin
    if checkout:
        payload['checkout'] = checkout

    if payload:
        return requests.get(_url('/booking/'), params=payload)
    else:
        return requests.get(_url('/booking/'))


def describe_booking(booking_id):
    return requests.get(_url('/booking/{:d}/'.format(booking_id)))


def add_booking(firstname = 'Jim', lastname = 'Brown', totalprice = 111, depositpaid = True, checkin = '2018-01-01', checkout = '2019-01-01', additionalneeds = 'Breakfast'):
    return requests.post(_url('/booking/'), json={
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : depositpaid,
        "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkin
        },
        "additionalneeds" : additionalneeds
    })


def remove_booking(booking_id):
    return requests.delete(_url('/bookings/{:d}/'.format(booking_id)))


def update_booking(booking_id, summary, description):
    url = _url('/bookings/{:d}/'.format(booking_id))
    return requests.put(url, json={
        'summary': summary,
        'description': description,
    })
