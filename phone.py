
print("---------------------------------------------------------\nWELCOME TO THE EMAIL VALIDATION TOOL\n---------------------------------------------------------")

print("Please begin by entering your E-Mail body text, sender's E-Mail ID and any phone numbers given below")
body = str(input("Copy and paste the body of the E-Mail here:  "))
sender = str(input("Enter the E-Mail ID of the sender:  "))
number = int(input("Enter any phone numbers in the mail:  "))

def num(number):
     
     import phonenumbers
     print("Enter your phone number with the country code: ")
     print("For example: +91xxxxxxxxxx")
     number=str(input("Number with country code: "))

     if len(number)==13:
         from phonenumbers import geocoder 
         phone_number = phonenumbers.parse(number) 
         print("Country is: ",geocoder.description_for_number(phone_number,'en'))

         from phonenumbers import carrier 
         service_provider = phonenumbers.parse(number) 
         print("Carrier is: ",carrier.name_for_number(service_provider,'en'))
        
