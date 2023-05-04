
class Cars:
    def __init__(self,model,name,color,engine = False, x = 0,):
        self.name = name
        self.color = color
        self.engine = engine
        self.x = x
        self.model = model
    def engineon(self):
        self.engine = True
    def engineoff(self):
        self.engine = False
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
    
        
        
bmw = Cars('x5','bmw', 'black')
wolksvagen = Cars('polo','wolksvagen','blue')
lada = Cars('priora','lada','grey')
car = input('Выберете машину')
reap = 0
while reap <= 10:
    if input() == 'w':
        lada.move_vperiod()
        reap = reap + 1
    if input() == 's':
        reap = reap + 1
        lada.move_nazad()
    if input() == 'e':
        lada.engineon()
        reap = reap + 1
    if input() == 'q':
        lada.engineoff()
        reap = reap + 1

