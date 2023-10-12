x = int(input("Введите X "))
y = int(input("Введите Y"))

if (x > 0) and (y > 0) :
    print("Точка находится в I четверти")
elif x < 0 and y > 0 :
    print("Точка находится во II Четверти")
elif x < 0 and y < 0 :
    print("Точка находится в III четверти")
elif x > 0 and y < 0 :
    print("ТОчка находится в IV четверти")
elif x == 0 :
    print("Точка лежит на прямой Y")
elif y == 0 :
    print("Точка лежит на прямой Х")
elif x == 0 and y == 0 :
    print("Точка лежит в начале координат")


