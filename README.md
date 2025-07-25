Task 1: Read a File and Handle Errors 

my_dict = {'nikhil':57,'raju':70,'vinay':80}
student = input('Enter a student\'s name: ')
if student in my_dict:
    print('{} , marks: {}'.format(student,my_dict[student]))
else:
    print('Student not found')


Task 2: Write and Append Data to a File

my_list = [1,2,3,4,5,6,7,8,9,10]
print('Original list:',my_list)
k=my_list[0:5]
print('Extracted first five elements:',k)
k.reverse()
print('Reversed extracted element: ',k)

