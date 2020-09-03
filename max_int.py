listi = []
max_int = 0
num_int = 0
while num_int >= 0:
    listi.append(num_int)
    max_int = max(listi)
    num_int = int(input("Input a number: ")) 
print("The maximum is", max_int)
#Bý til while lykkju
#Bý til lista til að geta safnað inputunum
#Ef að tala er lægri eða jafnt og núll þá hættir
#loopan að taka inn tölur