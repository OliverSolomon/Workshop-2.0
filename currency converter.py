# currency converter
# convert between USD, Kes
print('       \n')

print('CURRENCY CONVERTER')
print('------------------')

print('       \n')

currency = input('Enter the currency you want to convert Kes(K) / USD(USD): ')
amount = input('Enter the amount you want to convert: ')

float_amount = float(amount)

if currency == 'K':
    print('The amount in USD is: ', float_amount * 0.0095)
elif currency == 'USD':
    print('The amount in Kes is: ', float_amount * 129)




































