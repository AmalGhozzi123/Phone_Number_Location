# Import the necessary modules from the phonenumbers library
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Print a separator for better readability
print("x" * 50)

# Prompt the user to enter a phone number and store the input
entered_num = input("Please enter a phone number: ")

# Create a PhoneNumber object from the entered number
# The second parameter 'None' means the library will infer the region from the input
phone_num = phonenumbers.parse(entered_num, None)
# Alternatively, you can specify a region code, e.g., "EG" for Egypt
# phone_num = phonenumbers.parse(entered_num, "EG")

# Print the parsed PhoneNumber object to show its details
print(phone_num)

# Retrieve and print the geographic description (location) of the phone number in Arabic
print(geocoder.description_for_number(phone_num, "en"))

# Retrieve and print the name of the carrier that originally owned the phone number in English
print(carrier.name_for_number(phone_num, "en"))

# Retrieve and print a list of time zones that the phone number potentially belongs to
print(timezone.time_zones_for_number(phone_num))
