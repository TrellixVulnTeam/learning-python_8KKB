# prompt = "Tell me something about you:"
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


prompt = "Tell me something about you:"

while True:
    message = input(prompt)

    if message == 'quit':
        break
    print(message)
