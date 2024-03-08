# prompts user for age
age = int(input('Enter age: '))
print('''Employment statues:
      Enter: e for employed
             u for unemployed
             s for student''')
# prompts user for employement statues
statues = input(': ')
overall_price = int(input('R: '))

# run code when user is under 18 & a student
if age <= 18 and statues == 's':
    print('37 percent discount!')
    # calculate the discount price
    discount = overall_price * (37/100)
    # subtract discount price to original price for the discounted price
    print('Your price is: ', (overall_price - discount))

# run code when user is over 18 & a student
elif age > 18 and statues == 's':
    print('30 percent discount!')
    discount = overall_price * (30/100)
    print('Your price is: ', (overall_price - discount))

# run code when user is under 18 & unemployed
elif age <= 18 and statues == 'u':
    print('25 percent discount!')
    discount = overall_price * (25/100)
    print('Your price is: ', (overall_price - discount))

# run code when user is under 18 & employed
elif age < 18 and statues == 'e':
    print('20 percent discount')
    discount = overall_price * (20/100)
    print('Your price is: ', (overall_price - discount))

# run code when user is over 18 & unemployed
elif age > 18 and statues == 'u':
    print('15 percent discount')
    discount = overall_price * (15/100)
    print('Your price is: ', (overall_price - discount))

# run code when user is over 18 & employed
elif age >= 18 and statues == 'e':
    print('10 percent discount')
    discount = overall_price * (37/100)
    print('Your price is: ', (overall_price - discount))

