print("Введите чиcло:")
arab = int(input())
rom = ""
while arab >= 1000:
        arab = arab-1000
        rom = rom + "M"
else: 
        while arab >= 500: 
            arab = arab -500
            rom = rom + "D"
        else:
            while arab >= 100:
                arab = arab -100
                rom = rom + "C"
                if "DCCCC" in rom:
                    rom = rom.replace("DCCCC","CM")
            else:
                while arab >= 50:
                    arab = arab -50
                    rom = rom + "L"
                else:
                    while arab >= 10:
                        arab = arab -10
                        rom = rom + "X"
                        if "XXXX" in rom:
                            rom = rom.replace("XXXX","XL")
                    else:
                        while arab >= 5:
                            arab = arab -5
                            rom = rom + "V"
                        else:
                            while arab >= 1:
                                arab = arab -1
                                rom = rom + "I"
                                if "VIIII" in rom:
                                    rom = rom.replace("VIIII", "IX") 
print("Римское чиcло:", rom)
