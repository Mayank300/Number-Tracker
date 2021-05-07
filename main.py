from phonenumbers import timezone
from phonenumbers import carrier
import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))


service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))


tm_number = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(tm_number))
