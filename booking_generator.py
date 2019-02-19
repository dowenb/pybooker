#booking_generator.py
from random import choice

def GenerateBooking():
    firstname = choice(['Bart', 'Maggie', 'Lisa', 'Marge', 'Homer', 'Wayland'])
    lastname = choice(['Simpson', 'Smithers', 'Burns', 'Krustofsky'])
    totalprice = choice([111,112,113,114,115,116,200,999])
    depositpaid = choice([True, False])
    checkin = choice(['2018-02-01','2018-03-01','2018-04-01','2018-05-01','2018-06-10'])
    checkout = choice(['2018-02-5','2018-03-05','2018-04-05','2018-05-05','2018-06-20'])
    additionalneeds = choice(['Breakfast', 'Mini Fridge', 'Extra towel', 'Dinner'])
    
    return(
        {
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : depositpaid,
        "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
        },
        "additionalneeds" : additionalneeds
        }
    )