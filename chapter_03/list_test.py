# names = ['刘安光', '杜安平', '付山稞']
# print(names[0])
# print(names[1])
# print(names[2])
#
# messages = ['你好吗？', '你怎么了？', '你写作业了吗？']
#
# print(names[0] + messages[1])
# print(names[1] + messages[2])
# print(names[2] + messages[0])
ask=['刘安光','杜安平','付晓宇','付山稞']
ask.insert(0,'黄妍')
print(ask)
ask.append('黄一梦')
print(ask)
del ask[0]
print(ask)
ask.remove('付晓宇')
print(ask)
ask[0] = '刘飞扬'
print(ask)
he = ask.pop()
print(he)
print(ask)