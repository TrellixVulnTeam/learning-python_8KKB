# players = ['刘安光','黄妍','付山稞','郑帆','付晓宇']
# print(players)
# players_sp = players[0:-1]
#
# print(players_sp)

# players = ['刘安光','黄妍','付山稞','郑帆','付晓宇']
# 两个列表变量实际上指示的是同一个列表
# s = players
# print(s)
# players[0] = '111'
# s.append("231")
# print(s)
# print(players)

players = ['刘安光', '黄妍', '付山稞', '郑帆', '付晓宇']

# 通过切片拷贝列表（形成一个新的列表），是两个列表
s = players[:]

print(s)
print(players)

s[0]='s0'
players[0]='player0'
s[1]='s1'

print(s)
print(players)
