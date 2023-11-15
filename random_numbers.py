import random
#define main function
def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
# define the  append random numbers function
def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_number = round(random_number, 1)
        numbers_list.append(rounded_number)

#Run program
if __name__ == '__main__':
    main()