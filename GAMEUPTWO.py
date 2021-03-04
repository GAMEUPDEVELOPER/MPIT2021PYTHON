import arcade as ar
import random

WIDTH = 1040
HEIGHT = 640
TITLE = 'GAMEUP'

player_width = 50
player_height = 50

bot_width = 50
bot_height = 50

class Bubble:
    def __init__(self):
        # начальные координаты
        self.center_x = random.randrange(160,880)
        self.center_y = 320
            
        # начальная скорость
        self.change_x = random.randrange(-15, 15, 10)
        self.change_y = random.randrange(-15, 15, 10)

        self.color = ar.color.BLUE

        self.radius = 20

    # функция зарисовки фигуры
    def draw(self):
                               #    300            300     50 20 ar.color.GREEN_YELLOW
        ar.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    # фенкция движения
    def update(self):
        # алгоритм движения  
        self.center_x += self.change_x
        self.center_y += self.change_y

class Bot:
    def __init__(self,x = 950,y = 350):
        # начальные координаты
        self.center_x = x
        self.center_y = y
            
        # начальная скорость
        self.change_x = 0
        self.change_y = 0

        self.color = ar.color.BLACK

    # функция зарисовки фигуры
    def draw(self):
        ar.draw_ellipse_filled(self.center_x, self.center_y,50,100,ar.color.ORANGE)
                               #    300            300      50 20  ar.color
        ar.draw_circle_filled(self.center_x, self.center_y,20,self.color)



    # функция движения
    def update(self):
        # алгоритм движения
        self.center_x += self.change_x
        self.center_y += self.change_y

        # условие границы сверху
        if self.center_y > 640 - 10:
            self.center_y = 640 - 10
        
        if self.center_y < 0 + 10:  
            self.center_y = 0 + 10
        # границы по сторонам
        if self.center_x > 1040 - 10:  
            self.center_x = 1040 - 10

        if self.center_x < 520 + 10:  
            self.center_x = 520 + 10

class Player:
    
    def __init__(self,x = 50,y = 350):
        # началные координаты
        self.center_x = x
        self.center_y = y
            
        # начальная скорость
        self.change_x = 0
        self.change_y = 0

        self.color = ar.color.BLACK

    # функция зарисовки фигуры
    def draw(self):
        ar.draw_ellipse_filled(self.center_x, self.center_y,50,100,ar.color.LIGHT_GREEN)
                               #    300            300      50 20  ar.color
        ar.draw_circle_filled(self.center_x, self.center_y,20,self.color)

    # фенкция движения
    def update(self):
        # алгоритм движения
        self.center_x += self.change_x
        self.center_y += self.change_y

        # условие границы сверху
        if self.center_y > 640 - 10:
            self.center_y = 640 - 10
        
        if self.center_y < 0 + 10:  
            self.center_y = 0 + 10
        # границы по сторонам
        if self.center_x > 520 - 10:  
            self.center_x = 520 - 10

        if self.center_x < 0 + 10:  
            self.center_x = 0 + 10

# основной class
class Mygame(ar.Window):
    # метод(функция) инициализации (создания переменных)
    def __init__(self,w,h,t):
        super().__init__(w,h,t)

        self.player = None

        self.bot = None

        self.bubble = None

        self.record = 0

        self.recordtwo = 0

    # метод установки начальных значений
    def setup(self):
        ar.set_background_color(ar.color.BLUE_SAPPHIRE)

        self.count = 0

        self.counttwo = 0

        self.player = Player()

        self.bot = Bot()

        self.bubble = Bubble()
    # метод зарисовки
    def on_draw(self):
        ar.start_render()

        ar.draw_text(f'счет:{self.count}',50,550,ar.color.YELLOW_GREEN,18)

        ar.draw_text(f'счет:{self.counttwo}',950,550,ar.color.YELLOW_GREEN,18)

        self.player.draw()

        self.bot.draw()

        self.bubble.draw()

    # метод обновления внутри игры
    def update(self,delta_time):
        pass

        self.bot.update()
        if self.counttwo >= self.recordtwo:
            self.recordtwo = self.counttwo
        
        self.player.update()
        if self.count >= self.record:
            self.record = self.count

        self.bubble.update()

        distance_x = ((self.bubble.center_x - self.player.center_x)**2)**0.5
        distance_y = ((self.bubble.center_y - self.player.center_y)**2)**0.5

        sum_dist_x = self.bubble.radius + player_width/2
        sum_dist_y = self.bubble.radius + player_height/2

        if sum_dist_x > distance_x and sum_dist_y > distance_y:
            self.bubble.change_x *= -1.1
        if self.bubble.center_x < 0:
            self.counttwo += 1
            self.bubble.__init__()


        distance_x = ((self.bubble.center_x - self.bot.center_x)**2)**0.5
        distance_y = ((self.bubble.center_y - self.bot.center_y)**2)**0.5

        sum_dist_x = self.bubble.radius + bot_width/2
        sum_dist_x = self.bubble.radius + bot_height/2

        if sum_dist_x > distance_x and sum_dist_y > distance_y:
            self.bubble.change_x *= -1.1
        if self.bubble.center_x > WIDTH:
            self.count += 1
            self.bubble.__init__()

    # метод управления клавиатурой
    def on_key_press(self,key,modifiers):
        if key == ar.key.W:
            self.player.change_y = 10
        if key == ar.key.S:
            self.player.change_y = -10
        if key == ar.key.A:
            self.player.change_x = -10
        if key == ar.key.D:
            self.player.change_x = 10

        if key == ar.key.UP:
            self.bot.change_y = 10
        if key == ar.key.DOWN:
            self.bot.change_y = -10
        if key == ar.key.LEFT:
            self.bot.change_x = -10
        if key == ar.key.RIGHT:
            self.bot.change_x = 10

    # метод для остановки игрока если нет нажатия
    def on_key_release(self,key,modifiers):
        if key == ar.key.W:
            self.player.change_y = 0
        if key == ar.key.S:
            self.player.change_y = 0
        if key == ar.key.A:
            self.player.change_x = 0
        if key == ar.key.D:
            self.player.change_x = 0

        if key == ar.key.UP:
            self.bot.change_y = 0
        if key == ar.key.DOWN:
            self.bot.change_y = 0
        if key == ar.key.LEFT:
            self.bot.change_x = 0
        if key == ar.key.RIGHT:
            self.bot.change_x = 0
     
# основная функция
def main():
    # присвоение к переменной основнго класса
    window = Mygame(WIDTH,HEIGHT,TITLE)
    window.setup()
    ar.run()

# вызов функции

main()
