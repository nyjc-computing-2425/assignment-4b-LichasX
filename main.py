stdform = input('Enter a number in scientific notation: ').strip()
valid_chars = "0123456789Ex.-^"
check = True
for char in stdform:
  if not char in valid_chars:
    check = False
if stdform.find(" ") == -1 and stdform.count(".") <= 1 and stdform.count("x") <= 1 and stdform.count("^") <= 1 and int(stdform[stdform.find("^")+1::]) % 1 == 0 and check == True:
  output = stdform[0:stdform.find("x10^")] + "E" + stdform[stdform.find("^")+1::]
  print(f"This number in E notation is {output}.")
else:
  print("Error converting to scientific E notation.")
