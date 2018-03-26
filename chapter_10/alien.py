file_name = 'alien.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except:
    print("找不到该文件！")
