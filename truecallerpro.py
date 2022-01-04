import phonenumbers
from phonenumbers import timezone,geocoder,carrier
pn=input("Enter phone number: ")
phoneN= (phonenumbers.parse(pn))
timeZone=timezone.time_zones_for_number(phoneN)
car=carrier.name_for_number(phoneN,'en')

reg=geocoder.description_for_number(phoneN,'en')

print(phoneN)
print(timeZone)
print(car)
print(reg)