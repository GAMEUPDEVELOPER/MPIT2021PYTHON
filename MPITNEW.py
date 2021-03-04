import arcade as ar
import random

WIDTH = 1000
HEIGHT = 600

TITLE = 'EDCGAMEPLAY'

# основной class
class Mygame(ar.Window):
    # метод(функция) инициализации (создания переменных)
    def __init__(self,w,h,t):
        super().__init__(w,h,t)

        self.fon = 1
        self.player = None
        self.magnit_list = None
        self.magnitred_list = None
        self.wall_list = None
        self.answerone = None
        self.answertwo = None
        self.answer = None
        self.fonone = None
        self.fontwo = None
        self.fonthree = None
        self.fonfour = None
        self.fonfive = None
        if self.fon == 4:
            self.Physics_engine = None

        self.count = None
        self.counttwo = None
    # метод установки начальных значений
    def setup(self):
        ar.set_background_color(ar.color.DARK_GREEN)

        self.count = 0
        self.counttwo = 0

        self.fonone = ar.SpriteList()
        self.player = ar.SpriteList()
        self.magnit_list = ar.SpriteList()
        self.magnitred_list = ar.SpriteList()
        self.wall_list = ar.SpriteList()
        self.answerone = ar.SpriteList()
        self.answertwo = ar.SpriteList()
        self.answer = ar.SpriteList()
        self.fontwo = ar.SpriteList()
        self.fonthree = ar.SpriteList()
        self.fonfour = ar.SpriteList()
        self.fonfive = ar.SpriteList()

        if self.fon == 1:
            self.fonone = ar.Sprite('gameup\Новый хлс.png',0.7)
            self.fonone.center_x = 500
            self.fonone.center_y = 300

        if self.fon == 2:
            self.fontwo = ar.Sprite('gameup\Новый хлс.png',0.7)
            self.fontwo.center_x = 500
            self.fontwo.center_y = 300

        if self.fon == 3:
            self.fonthree = ar.Sprite('gameup\Новый хлс.png',0.7)
            self.fonthree.center_x = 500
            self.fonthree.center_y = 300

        if self.fon == 4:
            # магниты
            for i in range(10): 
                for j in range(10): 
                    magnit = ar.Sprite('gameup\magnit.png',0.05)
                    magnit.center_x = 48 + i * 120
                    magnit.center_y = 48 + j * 120
                    self.magnit_list.append(magnit)

            # красные магниты
            for i in range(10):
                for j in range(10): 
                    magnitred = ar.Sprite('gameup\magnitred.png',0.05)
                    magnitred.center_x = 58 + i * 130  
                    magnitred.center_y = 58 + j * 130
                    self.magnitred_list.append(magnitred)

            # стена вправо по низу
            for i in range(20):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 29 + i * 57
                wall.center_y = 16
                self.wall_list.append(wall)

            # стена вправо по верху
            for i in range(20):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 29 + i * 57
                wall.center_y = 575
                self.wall_list.append(wall)

            # стена вверх по правой стороне
            for i in range(20):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 1120
                wall.center_y = 16 + i * 50
                self.wall_list.append(wall)

            # стена вверх по левой стороне
            for i in range(20):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 150 
                wall.center_y = 32 + i * 50
                self.wall_list.append(wall)

            # стена 1
            for i in range(5):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 320 
                wall.center_y = 32 + i * 50
                self.wall_list.append(wall)

            # стена 2
            for i in range(9):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 960
                wall.center_y = 580 - i * 50
                self.wall_list.append(wall)

            # стена 3
            for i in range(11):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 290 + i * 50
                wall.center_y = 400
                self.wall_list.append(wall)

            # стена 4
            for i in range(8):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 500 
                wall.center_y = 50 + i * 50
                self.wall_list.append(wall)

            # стена 5
            for i in range(5):
                wall = ar.Sprite('gameup\мел (1).png',0.25)
                wall.center_x = 750
                wall.center_y = 32 + i * 50
                self.wall_list.append(wall)

            # игрок
            self.player = ar.Sprite('gameup\игрок.png',0.05)
            self.player.center_x = 600
            self.player.center_y = 200

        if self.fon == 5:
            self.fonfive = ar.Sprite('gameup\Новый хлс.png',0.7)
            self.fonfive.center_x = 500
            self.fonfive.center_y = 300

        if self.fon == 4:
            self.Physics_engine = ar.PhysicsEngineSimple(self.player,self.wall_list)
    # метод зарисовки
    def on_draw(self):
        ar.start_render()
        if self.fon == 1:
            self.fonone.draw()
            ar.draw_text('Оонньуохха',200,280,ar.color.WHITE,100)
        if self.fon == 4:
            self.player.draw()
            self.magnit_list.draw()
            self.magnitred_list.draw()
            self.wall_list.draw()
            self.fonfour.draw()
            ar.draw_text(f'от кYех магниттар:{self.count}',800,500,ar.color.BLUE,15)
            ar.draw_text(f'кыhыл магниттар:{self.counttwo}',600,500,ar.color.BLUE,15)
            ar.draw_text('Хас кыhыл уонна от кYех магнит баарый?',50,500,ar.color.RED,15)
        if self.fon == 2:
            self.fontwo.draw()
            self.answerone.draw()
            ar.draw_text('2+6 хас буоларый?',300,400,ar.color.WHITE_SMOKE,35)
            ar.draw_text('9-4 хас буоларый?',300,350,ar.color.WHITE_SMOKE,35)
            ar.draw_text('5+4-1 хас буоларый?',300,300,ar.color.WHITE_SMOKE,35)
            ar.draw_text('9-5+(3-3) хас буоларый?',300,250,ar.color.WHITE_SMOKE,35)
            ar.draw_text('5+(3+5-2) хас буоларый?',300,200,ar.color.WHITE_SMOKE,35)
        if self.fon == 3:
            self.answertwo.draw()
            self.answer.draw()
            self.fonthree.draw()
            ar.draw_text('2*5хас буоларый?',300,400,ar.color.WHITE_SMOKE,35)
            ar.draw_text('9*2 хас буоларый?',300,350,ar.color.WHITE_SMOKE,35)
            ar.draw_text('3*2+4 хас буоларый?',300,300,ar.color.WHITE_SMOKE,35)
        if self.fon == 5:
            self.fonfive.draw()
            ar.draw_text('2+6=8',300,450,ar.color.GREEN,35)
            ar.draw_text('9-4=5',300,400,ar.color.GREEN,35)
            ar.draw_text('5+4-1=8',300,350,ar.color.GREEN,35)
            ar.draw_text('9-5+(3-3)=4',300,300,ar.color.GREEN,35)
            ar.draw_text('5+(3+5-2)=11',300,250,ar.color.GREEN,35)
            ar.draw_text('2*5=10',300,200,ar.color.GREEN,35)
            ar.draw_text('9*2=18',300,150,ar.color.GREEN,35)
            ar.draw_text('3*2+4=10',300,100,ar.color.GREEN,35)
            ar.draw_text('10 кыhыл уонна 20 от кYех магнит баар, уопсайа 30 магнит баар',300,50,ar.color.GREEN,15)
    # метод обновления внутри игры
    def update(self,delta_time):
        if self.fon == 4:
            self.Physics_engine.update()

        for magnitred in self.magnitred_list:
            if ar.check_for_collision_with_list(magnitred,self.wall_list):
                magnitred.remove_from_sprite_lists()

            if ar.check_for_collision(magnitred,self.player):
                magnitred.remove_from_sprite_lists()
                self.counttwo +=1 

        for magnit in self.magnit_list:
            if ar.check_for_collision_with_list(magnit,self.wall_list):
                magnit.remove_from_sprite_lists()

            if ar.check_for_collision(magnit,self.player):
                magnit.remove_from_sprite_lists()
                self.count +=1 

        pass
    # метод управления клавиатурой
    def on_key_press(self,key,modifiers):
        if self.fon == 4:
            if key == ar.key.W:
                self.player.change_y = 10
            if key == ar.key.S:
                self.player.change_y = -10
            if key == ar.key.D:
                self.player.change_x = 10
            if key == ar.key.A:
                self.player.change_x = -10
        
        pass
    # метод для остановки игрока если нет нажатия
    def on_key_release(self,key,modifiers):
        if self.fon == 4:
            if key == ar.key.W:
                self.player.change_y = 0
            if key == ar.key.S:
                self.player.change_y = 0
            if key == ar.key.D:
                self.player.change_x = 0
            if key == ar.key.A:
                self.player.change_x = 0
        
        pass 

# основная функция
def main():
    # присвоение к переменной основнго класса
    window = Mygame(WIDTH,HEIGHT,TITLE)
    window.setup()
    ar.run()
    
# вызов функции
main()