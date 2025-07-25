my_dict = {'nikhil':57,'raju':70,'vinay':80}
student = input('Enter a student\'s name: ')
if student in my_dict:
    print('{} , marks: {}'.format(student,my_dict[student]))
else:
    print('Student not found')