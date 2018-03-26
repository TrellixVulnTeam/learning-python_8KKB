# alien_o = {'color': 'green', 'points': 5}
# alien_o['score'] = 55
# print(alien_o['color'])
# print(alien_o['points'])
# print(alien_o)

# alien_o = {'color': 'green', 'points': 5}
# print(alien_o['color'])
# alien_o['color'] = 'red'
# print(alien_o['color'])


alien_o = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
print("Original x-position: " + str(alien_o['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
speed = alien_o['speed']
if speed == 'slow':
    x_increment = 1
elif speed == 'medium':
    x_increment = 2
else:
    x_increment = 3

# 新位置等于老位置加上增量
alien_o['x_position'] = alien_o['x_position'] + x_increment
print("New x-position: " + str(alien_o['x_position']))

del alien_o['x_position']
print(alien_o)
