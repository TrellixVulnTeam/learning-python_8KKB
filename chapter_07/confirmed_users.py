# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace','cat']
confirmed_users = []

# 验证每个用户，直到没有未验证用户，将每个经过验证的用户都添加到已验证的用户中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有验证过的用户
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# 删除特定用户
while 'cat' in confirmed_users:
    confirmed_users.remove('cat')
print(confirmed_users)