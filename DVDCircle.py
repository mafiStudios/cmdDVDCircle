cmdX,cmdY = 120,30 #Разрешение cmd
screen = dict()
empty,symb = " ","@"
r = 8 #Радиус круга.(Примерно)

#Соотношение
ratio = cmdX/cmdY+8/16-1 #Чтобы круг был круглым.1-соотношение cmd,2-символа
x0,y0 = cmdX/2,cmdY/2 # Нули относительно графика
cx,cy = 0,0 #Координаты центра круга
horiz, vertic = False,False #Направление мяча. Horiz True - право, Vertic True - вверх
for frames in range(0,50000):
    for y in range(0,cmdY):
        for x in range(0,cmdX):
            i = cmdX*(y-1)+x        # i - Символ по счёту.
            CenY,CenX = y0-i//cmdX, x0-i%cmdX      #Центр графика

            if cy>=cmdY/2-r:vertic = False
            elif cy<=-(cmdY/2-r-1):vertic = True
            
            if cx>=cmdX/2-r*2+2:horiz = False
            elif cx <=-(cmdX/2-r*2+0.5):horiz = True
        
            if vertic == False: cy-= 0.00002
            elif vertic == True: cy += 0.00002
            
            if horiz == True: cx += 0.00004
            elif horiz == False: cx -= 0.00004

            screen[i] = empty #Заполнение пустотой
            if (CenY-cy)**2 + (CenX-cx)**2/ratio <= r**2:screen[i] = symb   #Круг через формулы
            
    for value in screen.values():print(value,end="")    #Вывод
    fullscreen = ""
    for value in screen.values():fullscreen += str(value)
    else:print(fullscreen,end="")
