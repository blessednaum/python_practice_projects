def categorise_age(age):
 if age < 0:
    return "invalid age"
 elif age <=9:
    return "Generation Alfa"

 elif age <=24:
    return "Generation Genz"

 elif age <=34:
    return "Generation Minnelials"
 elif age <=73:
    return "Baby Burmers"

 else:
  return "silent Generation"

  def main():
  
     age = int(input("enter your name"))
     generation = categorise_age(age)
     print (f"you belong to: {generation}") 
     
   # except valueError:
   #  print ("please put a valid age")
if _name_ == "_main":
        main()
