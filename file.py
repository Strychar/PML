def action(a,b,c):
 if a+b>c:
  print("no")
  return False
 elif a+c > b:
  print("no")
  return False
 elif b+c>a:
  print("no")
  return False
 else:
  print("yes")
  return True