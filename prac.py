weight = int(input("enter your weight here  "))
form = input("wight in kgs or g  " )
if form.upper() == "K":
    converted = weight * 0.45
    print("your weight is", str(converted), "in g")
else:
    converted = weight / 0.45
    print("your weight is", str(converted), "in kgs")