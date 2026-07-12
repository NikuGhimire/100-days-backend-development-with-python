#AND
age = 19
has_license = True
if age >=18 and has_license:
   print("is eligible: to drive")

   #OR
   age = 21
   has_license = False
if age >=18 or has_license:
     print("is eligible: to drive")

     #NOT
age = 23
has_license = False 
if age >=18 and not has_license:
    print("get a License 1st")

