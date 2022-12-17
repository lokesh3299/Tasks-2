from termcolor import colored

for num in range(1,201):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                if num % 10 == 0:
                    print(num)
                else:
                    print(num , end="   ")
                break
        else:
              print(colored(num , 'yellow'), end="   ")
    else:
        print(num, end = '  ')