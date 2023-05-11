import keyboard
import turtle
class Cars:
    def __init__(self,model,name,color,engine = False, x = 0,):
        self.name = name
        self.color = color
        self.engine = engine
        self.x = x
        self.model = model
    def engineon(self):
        self.engine = True
        print('Двигатель включён')
    def engineoff(self):
        self.engine = False
        print('Двигатель выключен')
    def move_vperiod(self):
        if self.engine:
            self.x += 9
            print(f'Проехал {self.x}')
        else:
            print('Включи двигатель!!!!!!')
    def move_nazad(self):
        if self.engine:
            self.x -= 7
            print(f'Проехал назад {self.x}')
        else:
            print('Включи двигатель!!!!!!')
class Truck(Cars):
    def put(self):
        print('вы положили что то')
class Bike:
    def __init__(self,color,x) -> None:
        self.color = color
        self.x = x
    def move(self):
        self.x += 1
        print(f'Проехал 1 и оказался {self.x}')

    
        
        
bmw = Cars('x5','bmw', 'black')
wolksvagen = Cars('polo','wolksvagen','blue')
lada = Cars('priora','lada','grey')
kamaz = Truck('kamaz','black')
def choose_car():
    car = input('Выберете машину')
    if car == 'bmw':
        reap = 0
        while reap <=10:
            a = input()
            if a == 'w':
                bmw.move_vperiod()
                reap = reap + 1
            if a == 's':
                bmw.move_nazad()
                reap = reap + 1
            if a == 'e':
                bmw.engineon()
                reap = reap + 1
            if a == 'q':
                bmw.engineoff()
                reap = reap + 1
    if car == 'lada':
        reap = 0
        while reap <=10:
            a2 = input()
            if a2 == 'w':
                lada.move_vperiod()
                reap = reap + 1
            if a2 == 's':
                lada.move_nazad()
                reap = reap + 1
            if a2 == 'e':
                lada.engineon()
                reap = reap + 1
            if a2 == 'q':
                lada.engineoff()
                reap = reap + 1
    if car == 'wolksvagen':
        reap = 0
        while reap <=10:
            a3 = input()
            if a3 == 'w':
                wolksvagen.move_vperiod()
                reap = reap + 1
            if a3 == 's':
                wolksvagen.move_nazad()
                reap = reap + 1
            if a3 == 'e':
                wolksvagen.engineon()
                reap = reap + 1
            if a3 == 'q':
                wolksvagen.engineoff()
                reap = reap + 1
#choose_car()