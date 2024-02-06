print("Welcome to the calculator!")
num1 = int(input("Please enter your first number: "))
operator = input("Enter the operator here. ")
num2 = int(input("Please enter your second number: "))

if operator == '+':
	print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
	print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
	print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
	if num2 == 0:
		print("Error! Cannot divide number by 0!")
	else:
		print(f"{num1} / {num2} = {num1 / num2}")
elif operator == "**":
	print(f"{num1} ** {num2} = {num1 ** num2}")
elif operator == "//":
	print(f"{num1} // {num2} = {num1 // num2}")
elif operator == "%":
	print(f"{num1} % {num2} = {num1 % num2}")
else:
	print(f"{operator} is not a valid operator!")






