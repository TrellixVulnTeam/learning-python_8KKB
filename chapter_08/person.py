def build_person(first_name, last_name):
    """ 返回一个字典，其中包含有关一个人的信息 """
    person = {'firstname':first_name, 'lastname':last_name}
    return person

my_name = build_person('angus', 'liu')
print(my_name)