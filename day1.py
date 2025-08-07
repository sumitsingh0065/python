name = input("What is your name? ")
print(f"Hello, {name}!")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("That's an even number.")
else:
    print("That's an odd number.")

print(f"Here are the numbers from 1 to {number}:")
for i in range(1, number + 1):
    print(i)
