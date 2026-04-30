#  type of optimize code
# Creating a strong Password
password=input("Enter your password: ")
if len(password)<8:
  print("Weak password: ")
elif not re.search("[A-Z]",password):
  print("Weak password due to not any uppercase")
elif not re.search("[a-z]",password):
  print("Weak password due to not any lowercase ")
elif not re.search("[0-9]",password):
  print("Weak password due to not any digit/number")
elif not re.search("[!@#$%^&]",password):
  print("Weak password due to not any uppercase")
else:
  print("Strong Password ")
