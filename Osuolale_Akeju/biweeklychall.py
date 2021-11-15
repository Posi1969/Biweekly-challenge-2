# Taking inputs from user
user_name = input('Enter your name: ')
user_age = int(input('How old are you: '))
user_month = input('Enter your birth month: ')
user_day = int(input('Enter the day: '))
gender = int(input('Enter your sex: \n for male, enter 1,\n for female, enter 2 '))
# Making consideration for the gender
if gender == 1:
    print('Good day Mr {}'.format(user_name))
elif gender == 2:
    print('Good day Mrs {}'.format(user_name))
else:
    print('Who are you?')
# calculating the ages and other variables
current_year = 2020
year_of_birth = current_year - user_age
print('According to the information provided \nYour date of birth is {}/{}/{}'.format(user_day, user_month, year_of_birth))
print('You are {}years old'.format(user_age))
#categorising the user by age
if user_age <= 1:
    print('Going by your age, you are an infant')
elif user_age <= 11:
    print('Going by your age, you belong to the children class')
elif user_age <= 17:
    print('Going by your age, you should be with the teens')
elif user_age <= 64:
    print('Going by your age, you are a full grown adult')
else:
    print('Going by your age, you are in the older adult class')
decade_age = user_age - 10
print('Your age 10years ago is ', decade_age,'years')
# calculating the next ages in five decades
for w in range(current_year, 2080, 10):
    user_age += 10
    print('In ', w, 'you will be', user_age, 'years old')

