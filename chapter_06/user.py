user_o = {
    'name': 'angus',
    'age': 21,
    'hobby': 'read',
    'old_name': 'angus'
}

for k, v in user_o.items():
    print("key:" + k, "value:" + str(v))

for k in user_o.keys():
    print(k)

# print(user_o.items())
# print(user_o.keys())
# print(user_o.values())

# 使用set方法取出相同的value
print(set(user_o.values()))
