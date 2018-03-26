print("Give me two numbers, aand I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_numbe = input("Second number:")
    if second_numbe == 'q':
        break
    try:
        anwser = int(first_number) / int(second_numbe)
    except ZeroDivisionError:
        print("You can't divided by zero!")
    else:
        print(anwser)
