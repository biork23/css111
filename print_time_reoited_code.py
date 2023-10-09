from datetime import datetime

# # print timestamps to see how long sections of code
# # take to run

# firstt_name = 'Ismael'
# print('task completed')
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print('task completed')
# print(datetime.datetime.now())
# print()

#function to print current date and time   
# def print_time():
#     print('task completed')
#     print(datetime.now())
#     print()
def print_time(task_name):
     print(task_name)
     print(datetime.now())
     print()

# first_name = 'Ismael'
# print_time()
first_name = 'Ismael'
print_time('printed first nme')

# for x in range(0,10):
#     print(x)
# print_time() 
# 
for x in range(0,10):
    print(x)
print_time('completed loop')     

