import phonenumbers 

print("enter your phone number with the country code")
print("for example: +91xxxxxxxxxx")
x=str(input("number with country code: "))

if len(x)==13:
    from phonenumbers import geocoder 
    phone_number = phonenumbers.parse(x) 
    print("country is: ",geocoder.description_for_number(phone_number,'en'))

    from phonenumbers import carrier 
    service_provider = phonenumbers.parse(x) 
    print("carrier is: ",carrier.name_for_number(service_provider,'en'))
else:
    print("enter valid number")















