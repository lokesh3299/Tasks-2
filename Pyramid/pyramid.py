number = int(input("Enter the rows value of the diamond:"))

for n in range(number-1):
  print((number-n) * ' ' + (1*n+1) * '🌸')

for n in range(number-1, -1, -1):
  print((number-n) * ' ' + (1*n+1) * '🌸')