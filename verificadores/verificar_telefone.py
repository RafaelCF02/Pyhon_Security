import phonenumbers
from phonenumbers import geocoder

phone = phonenumbers.parse(input("Digite o telefone no formato (+5511xxxxxxxxx): "))

print(geocoder.description_for_number(phone, 'pt'))
