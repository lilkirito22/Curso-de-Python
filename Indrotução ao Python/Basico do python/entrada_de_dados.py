while True:
  # Get user input
  num1 = float(input("Enter the first number: "))
  operator = input("Enter the operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  # Perform calculation based on operator
  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2
  else:
    print("Invalid operator!")
    continue

  # Print the result
  print("Result:", result)

  # Ask if the user wants to continue
  choice = input("Do you want to continue? (yes/no): ")
  if choice.lower() != "yes":
    break