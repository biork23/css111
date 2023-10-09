# This function will return the first initial of a name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someones name and return the initials
first_name = input('Enter your first name: ')
# first_name_initial = first_name[0:1]
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
# middle_name_initial = middle_name[0:1]
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
# last_name_initial = last_name[0:1]
last_name_initial = get_initial(last_name)

print('Your initial are; '+ first_name_initial + middle_name_initial + last_name_initial)

#Demostration parameterized function

def get_initial(name, force_uppercase=True):
    if force_uppercase : 
        initial = name[0:1].upper()
    else : 
        initial = name[0:1]
    return initial
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

print('Your initial is: '+ first_name_initial)
