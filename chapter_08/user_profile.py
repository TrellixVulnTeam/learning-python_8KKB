def build_profile(first, last, **user_info):
    """ 创建一个字典，其中包含用户的一切信息 """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


my_info = build_profile('angus', 'liu', age=19, addr='cd')
print(my_info)
