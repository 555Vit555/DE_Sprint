my_str = str(input("Введите строку:"))
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
i = 0
while len(my_str) > i:
      
    if my_str[i] == "(":
        count1 = count1 + 1 #счетчик откр. круглых скобок
        i = i + 1
    elif my_str[i] == ")":
            count2 = count2 +1 #счетчик закр. круглых скобок
            i =  i + 1  
            if count2 > count1:
                print("False")
                break
    elif my_str[i] == "[":
            count3 = count3 + 1 #счетчик откр. квад. скобок
            i = i + 1
    elif my_str[i] == "]":
            count4 = count4 +1 # счетчик закр. квад. скобок
            i = i + 1
            if count4 > count3:
                    print(False)
                    break
    elif my_str[i] == "{":
            count3 = count3 + 1 #счетчик откр. фиг. скобок
            i = i + 1
    elif my_str[i] == "}":
            count4 = count4 +1 # счетчик закр. фиг. скобок
            i = i + 1
            if count4 > count3:
                    print(False)
                    break
     
if count1 == count2 and count3 == count4 and count5 == count6:
            print("True")
else:
    print("False")                     
