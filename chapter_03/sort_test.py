# print(cities)
# c = sorted(cities)
# c.reverse()
# print(c)

# cities.sort()
# cities.reverse()
# print('---------')
# print(cities)
# print(len(cities))
cities = ['sh', 'bj', 'cd', 'cq', 'adly', 's', 'ere', 'qq']
# 追加一个新城市 cc
cities.append('cc')
print(cities)
# 插入一个新城市 ee,插到第一个
cities.insert(0,'ee')
print(cities)
# 删除第二个城市
del cities[1]
print(cities)
# 删除 cq
cities.remove('cq')
print(cities)
# 对他临时排序
print(sorted(cities))
print(cities)
# 对他本身排序
cities.sort()
print(cities)
# 颠倒
cities.reverse()
print(cities)
# 求长度
print(len(cities))