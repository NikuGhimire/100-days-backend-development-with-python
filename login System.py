correct_username = "Niku"
correct_password = "Niku 12345"
username = input("Enter your name:") 

if username == correct_username:
   password = input("Enter your password")
   if password == correct_password:
      print("login successful")
   else:
    print("Incorrect password")
else:
      print("Invalid Username")
