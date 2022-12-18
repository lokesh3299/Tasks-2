from colorama import Fore, Back, Style,init

init(convert=True)

for num in range(1,201):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                if num % 10 == 0:
                    if(len(str(num))==1):
                        print('  '+str(num))
                    elif(len(str(num))==2):
                        print(' '+str(num))
                    elif(len(str(num))==3):
                        print(str(num))
                else:
                    if(len(str(num))==1):
                        print('  '+str(num) , end="   ")
                    elif(len(str(num))==2):
                        print(' '+str(num) , end="   ")
                    elif(len(str(num))==3):
                        print(str(num) , end="   ")
                break
        else:
            if(len(str(num))==1):
                print(Fore.YELLOW + Back.LIGHTBLACK_EX+'  '+str(num), end="   ")
                print(Style.RESET_ALL, end='')
            elif(len(str(num))==2):
                print(Fore.YELLOW + Back.LIGHTBLACK_EX+' '+str(num), end="   ")
                print(Style.RESET_ALL, end='')
            elif(len(str(num))==3):
                print(Fore.YELLOW + Back.LIGHTBLACK_EX+str(num), end="   ")
                print(Style.RESET_ALL, end='')
    else:
        print('  '+str(num), end = "   ")