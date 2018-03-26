def greet_users(names):
    """ 向列表中每位用户都发出简单的问候 """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['Angus', 'Tom', 'Anliy']
greet_users(usernames)