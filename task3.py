# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

n = int(input("Введете ваше число "))
if n<100000 or n>999999:
    print("Число должно быть шестизначным")
else:
    if n//100000 + n//10000%10 + n//1000%10 == n//100%10 + n//10%10 + n%10:
        print("билет счастливый")
    else:
        print("билет не счастливый")