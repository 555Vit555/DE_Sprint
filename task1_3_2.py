from audioop import reverse


print("Ведите строку:")
string = input()
new_string = string.lower().replace(" ","")
if new_string == new_string[::-1]: print("строка - палиндром")
else: print("строка - не палиндром")
    