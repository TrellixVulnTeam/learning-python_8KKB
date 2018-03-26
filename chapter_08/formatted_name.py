# def get_formatted_name(first_name, last_name):
#     ''' 返回整洁的姓名 '''
#     full_name = first_name + '·' + last_name
#     return full_name.title()
#
#
# my_name = get_formatted_name('angus', 'liu')
# print(my_name)


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + '·' + middle_name + '·' + last_name
    else:
        full_name = first_name + '·' + last_name
    return full_name.title()
my_name = get_formatted_name('angus', 'liu')
print(my_name)
my_name = get_formatted_name('angus', 'liu', 'f')
print(my_name)


while True:
    print("(enter 'q' at any time to quit)")
    f_name = input('Fist name:')
    if f_name == 'q':
        break
    l_name = input('Last name:')
    if l_name == 'q':
        break
    print(get_formatted_name(f_name,l_name))
