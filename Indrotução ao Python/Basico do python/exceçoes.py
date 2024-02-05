try:
  # Code that may raise an exception
  result = 10 / 0  # Division by zero will raise a ZeroDivisionError
  print("Result:", result)  # This line won't be executed if an exception occurs

except ZeroDivisionError:
  # Code to handle the specific exception
  print("Error: Division by zero is not allowed")

except Exception as e:
  # Code to handle any other exceptions
  print("An error occurred:", str(e))

finally:
  # Code that will always be executed, regardless of whether an exception occurred or not
  print("Program execution completed")