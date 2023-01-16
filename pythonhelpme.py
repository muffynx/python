import pyautogui as pg
import time
import random
print('''
         1.Cook 10 times
         2.Sail 10 times
         3.Shadow spirit
         4.Harb
         5.Impel Down
         6.PlayGROUNDS
         7.GEM and JEWEL
         8.All blue
         ''')

def cook():
    time.sleep(1)
    pg.click(x=45, y=261)
    time.sleep(1)
    pg.click(x=392, y=438)
    for i in range(11):
        time.sleep(1)
        pg.click(x=615, y=492)
    time.sleep(1)
    pg.click(x=809, y=246)
    time.sleep(1)
    pg.click(x=1043, y=114)
def sail():
    time.sleep(1)
    pg.click(x=35, y=310)
    time.sleep(0.5)
    for i in range(11):
        pg.click(x=862, y=243)
    time.sleep(1)
    def getsail():
        position = [(472,524),(475,556)]
        for _ in range(10):
            selected_pst = random.choice(position)
            time.sleep(1)
            pg.click(selected_pst[0], selected_pst[1])
            time.sleep(1)
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
       
function = {1: cook, 2: sail,3:fastival}
while True:
    user_input = input('enter a number 1 and 5 to start my funciton ')
    if user_input.isalpha():
        break
    try:
        function[int(user_input)]()
    except (ValueError, KeyError):
        print('Invalid input. Please enter a number between 1 and 5')
