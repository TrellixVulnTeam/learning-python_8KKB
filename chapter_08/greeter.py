def greet_user(username):
    # print(id(username))
    # 显示简单的问候语
    print("Hello! " + username)
    username = ""
    print(username)

username = input("请输入你的名字:")
# print(id(username))
greet_user(username)

print(username)