#kütüphaneler 
import win32api,win32con
import time
 
 
#Değişkenler
AssaultRifleIron = [[-37, 52.3900], [12, 45], [-42.7, 42], [-58, 37], [0, 33], [0, 28], [34.5, 25], [22.5, 26],[42.5, 18], [36, 10], [39, 15], [39, 18], [28, 18], [24, 28], [5, 29], [-18, 32], [-30, 33],[-34, 32], [-36, 29], [-43, 24], [-45, 17], [-45, 8], [-42, 5], [-27, 14], [-18, 21],[0, 25], [0, 28], [40, 28], [52, 26], [47, 15], [37, 21]]
LR300AssaultRifleIron = [[-2, 25], [-8, 31], [-10, 33], [-14, 31], [-18, 25], [-16, 20], [-14, 12], [-15, 12],[20, 8], [19, 8], [17, 8], [15, 7], [10, 5], [0, 4], [-10, 4], [-9, 4], [-12, 3],[-17, 3], [-18, 3], [-18, 2], [-16, 2], [-16, 2], [-15, 2], [-7, 2], [-3, 2], [13, 2],[30, 2], [36, 3], [30, 3]]
MP5A4Iron = [[3, 40], [-5, 29], [18, 36], [28, 36], [34, 34], [34, 32], [-23, 24], [-14, 8], [-17, 9], [-18, 3],[-2, 8], [20, 8], [18, 8], [25, 4], [12, 2], [7, 0], [7, 1], [5, 5], [-45, 5], [-40, 5], [-30, 5],[-25, 2],[-15, 2], [-10, 2], [-15, 0], [15, 0], [-5, 10], [-2, -10], [25, 0], [10, 0]]
##########################
timerak = 0.001 #AK için sadece
timerlr = 0.011 # emfor
timermp5 = 0.005 # mepebeş
##########################
ak = AssaultRifleIron
lr = LR300AssaultRifleIron
mp5 = MP5A4Iron
sensitivity = float(input("Sensitivity... :")) #İnput olarak alman gereken değer.
 
 
def baslat():
    
    print("   ▄▄▄▄▀ ▄   █    █ ▄▄  ██   █▄▄▄▄ ")
    print("▀▀▀ █     █  █    █   █ █ █  █  ▄▀ ")
    print("    █  █   █ █    █▀▀▀  █▄▄█ █▀▀▌  ")
    print("   █   █   █ ███▄ █     █  █ █  █  ")
    print("  ▀    █▄ ▄█     ▀ █       █   █   ")
    print("        ▀▀▀         ▀     █   ▀    ")
    print("For Menu, Press END key !")
 
def mousemove(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y), 0, 0)
 
def lrdown():
    while True: #Benim efsanevi aktivasyon loopum
        for i in lr:
            if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) < 0:
                truex = ((i[0]/2)/sensitivity) # matematikleri
                truey = ((i[1]/2)/sensitivity) # matematikleri
                for x in range(8):
                    movex = (truex/8) # matematikleri
                    movey = (truey/8) # matematikleri
                    mousemove(int(movex), int(movey))
                    time.sleep(timerlr/8)
            elif win32api.GetAsyncKeyState(0x23) < 0:
                secimyap()
            else:
                break
 
def akdown():
    while True: #Benim efsanevi aktivasyon loopum
        for i in ak:
            if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) < 0:
                truex = ((i[0]/2)/sensitivity) # matematikleri
                truey = ((i[1]/2)/sensitivity) # matematikleri
                for x in range(8):
                    movex = (truex/8) # matematikleri
                    movey = (truey/8) # matematikleri
                    mousemove(int(movex), int(movey))
                    time.sleep(timerak/8)
            elif win32api.GetAsyncKeyState(0x23) < 0:
                secimyap()
            else:
                break
 
def mp5down():
    while True: #Benim efsanevi aktivasyon loopum
        for i in MP5A4Iron:
            if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) < 0:
                truex = ((i[0]/2)/sensitivity) # matematikleri
                truey = ((i[1]/2)/sensitivity) # matematikleri
                for x in range(8):
                    movex = (truex/8) # matematikleri
                    movey = (truey/8) # matematikleri
                    mousemove(int(movex), int(movey))
                    time.sleep(timermp5/8)
            elif win32api.GetAsyncKeyState(0x23) < 0:
                secimyap()
            else:
                break
                
 
def secimyap():
    x = int(input("Ak = 1 \nLR = 2 \nMp5 = 3\n-Pick a gun...: "))
    if x == 1:
        akdown()
    elif x ==2:
        lrdown()
    elif x == 3:
        mp5down()
    else:
        print("ERROR !")
        secimyap()
 
 
 
secimyap()