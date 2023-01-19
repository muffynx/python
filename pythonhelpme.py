import pyautogui as pg
import time
import random
print('''
         1.Cook 10 times
         2.Sail 10 times
         3.Festival
         4.Shadow spirit
         5.Harb
         6.Impel Down
         7.PlayGROUNDS
         8.GEM and JEWEL
         9.All blue
         ''')

def cook():
    time.sleep(1)
    pg.click(x=45, y=261)
    time.sleep(1)
    pg.click(x=392, y=438)
    for i in range(11):
        time.sleep(0.5)
        pg.click(x=615, y=492)
    time.sleep(1)
    pg.click(x=809, y=246)
    time.sleep(1)
    pg.click(x=1043, y=114)
def sail():
    time.sleep(1)
    pg.click(x=35, y=310)
    time.sleep(0.5)
    for x in range(11):
        time.sleep(0.8)
        pg.click(x=875, y=318)
    
    getsail()
def getsail():
    position = [(472,524),(475,556)]
    for _ in range(10):
        selected_pst = random.choice(position)
        time.sleep(0.5)
        pg.click(selected_pst[0], selected_pst[1])
        
def fastival():
    position = [(224,387),(452,387),(683,387),(906,387),(1138,387)]

    count = int(input(" How many times wanna loop "))

    for _ in range(count):
        
        selected_pst = random.choice(position)
        time.sleep(0.1)
        pg.click(selected_pst[0], selected_pst[1])
        time.sleep(0.8)
        pg.click(x=586, y=534)
        time.sleep(0.5)
def Shadowspirit():
    x = int(input("what times do you want spirt: "))
    time.sleep(0.5)
    pg.click(x=784, y=58) # open
    time.sleep(1)
    for i in range(x):
        time.sleep(1)
        pg.click(x=674, y=677)
        for a in range(2):
            time.sleep(3)
            pg.click(x=1259, y=555)
            time.sleep(3)
        time.sleep(1)
        pg.click(x=674, y=677)
    time.sleep(2)
    pg.click(x=1315, y=62) #exit
def Harb():
    time.sleep(1)
    pg.click(x=1235, y=115)
    time.sleep(1)
    pg.click(x=683, y=525)
    time.sleep(1)
    pg.click(x=1041, y=265)
    time.sleep(1)
    pg.click(x=621, y=509)
    time.sleep(2)
    pg.click(x=624, y=402)
    time.sleep(1)
    pg.click(x=1017, y=663)
    time.sleep(1)
    pg.click(x=668, y=442)
    time.sleep(1)
    pg.click(x=668, y=442)
    time.sleep(1)
    pg.click(x=1252, y=44)
    time.sleep(1)
    pg.click(x=1288, y=82)
    time.sleep(1)
def ImpelDown():
    pg.click(x=644, y=52)
    time.sleep(5)
    for i in range(2):
        pg.click(x=595, y=671)
    time.sleep(0.2)
    pg.click(x=1310, y=56)
    time.sleep(0.3)
def PlayGROUNDS():
    pg.click(x=569, y=57)
    time.sleep(2)
    pg.click(x=363, y=486)
    time.sleep(1)
    pg.click(x=747, y=603)
    time.sleep(1)
    pg.click(x=1026, y=135)
def GEMandJEWEL():
    pg.click(x=938, y=664)
    time.sleep(1.5)
    pg.click(x=739, y=427)
    time.sleep(1)
    pg.click(x=607, y=450)
    time.sleep(5)
    pg.click(x=1006, y=52)
    time.sleep(1)
    pg.click(x=888, y=565)
    time.sleep(1)
    pg.click(x=607, y=426)
    pg.click(x=607, y=426)
    time.sleep(1)
    pg.click(x=954, y=82)
    time.sleep(1)
    pg.click(x=1324, y=58)
    time.sleep(0.1)
def Allblue():
    pg.click(x=715, y=66)
    time.sleep(1)
    pg.click(x=417, y=247)
    for p in range(5):
        pg.click(x=341, y=229)
    time.sleep(1.5)
    pg.click(x=1326, y=63)
function = {1: cook, 2: sail,3:fastival,4:Shadowspirit,5:Harb,6:ImpelDown,7:PlayGROUNDS,
            8:GEMandJEWEL,9:Allblue}
while True:
    user_input = input('enter a number 1 and 5 to start my funciton ')
    if user_input.isalpha():
        break
    try:
        function[int(user_input)]()
    except (ValueError, KeyError):
        print('Invalid input. Please enter a number between 1 and 5')
