import arcade as ar 


WIDTH = 1000
HEIGHT = 600
# полноэкранный = 1366 на 768
TITLE = 'EDCGAMEPLAY'

# основной class
class Mygame(ar.Window):
    # метод(функция) инициализации (создания переменных)
    def __init__(self,w,h,t):
        super().__init__(w,h,t)

        self.fon = 3

        if self.fon == 2:
            self.fontwo = None
            self.answer = None

        if self.fon == 1:
            self.fonone = None

        if self.fon == 3:
            self.fona = None
            self.answera = None

    # метод установки начальных значений
    def setup(self):
        ar.set_background_color(ar.color.DARK_GRAY)

        self.fonone = ar.SpriteList()

        self.fontwo = ar.SpriteList()
        self.answer = ar.SpriteList()

        self.fona = ar.SpriteList()
        self.answera = ar.SpriteList()


        if self.fon == 1:
            self.fonone = ar.Sprite('gameup\Новый хлст.png',0.5)
            self.fonone.center_x = 500
            self.fonone.center_y = 300

        if self.fon == 2:
            self.fontwo = ar.Sprite('gameup\Новый хлс.png',0.5)
            self.fontwo.center_x = 500
            self.fontwo.center_y = 300

            self.answer = ar.Sprite('gameup\вопрос1.png',0.5)
            self.answer.center_x = 500
            self.answer.center_y = 300


        if self.fon == 3:
            self.fona = ar.Sprite('gameup\Новый холст.png',0.5)
            self.fona.center_x = 500
            self.fona.center_y = 300

            self.answera = ar.Sprite('gameup\вопрос2.png',0.5)
            self.answera.center_x = 500
            self.answera.center_y = 300

    # метод зарисовки
    def on_draw(self):
        ar.start_render()

        if self.fon == 1:
            self.fonone.draw()

        if self.fon == 2:    
            self.answer.draw()

        if self.fon == 3:
            self.fona.draw()
            self.answera.draw()

    # метод обновления внутри игры
    def update(self,delta_time):
        if self.fon == 1:
            self.fonone.update()

        if self.fon == 2:
            self.fontwo.update()
            self.answer.update()
        if self.fon == 3:
            self.fona.update()
            self.answera.update()
        pass

    # метод управления клавиатурой
    def on_key_press(self,key,modifiers):
        if self.fon == 1:
            if key == ar.key.SPACE:
                self.fon += 1
        if self.fon == 2:
            if key == ar.key.Q:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.W:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.E:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.R:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.T:
                ar.draw_text('ПРАВИЛЬНО',500,400,ar.color.GREEN,30)
                self.fon += 1
            if key == ar.key.Y:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
        if self.fon == 3:
            if key == ar.key.Q:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.W:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.E:
                ar.draw_text('ПРАВИЛЬНО',500,400,ar.color.GREEN,30)
                self.fon -= 2
            if key == ar.key.R:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.T:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.Y:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
        pass
    # метод для остановки игрока если нет нажатия
    def on_key_release(self,key,modifiers):
        if self.fon == 1:
            if key == ar.key.SPACE:
                self.fon += 1
        if self.fon == 2:
            if key == ar.key.Q:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.W:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.E:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.R:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.T:
                ar.draw_text('ПРАВИЛЬНО',500,400,ar.color.GREEN,30)
                self.fon += 1
            if key == ar.key.Y:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
        if self.fon == 3:
            if key == ar.key.Q:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.W:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.E:
                ar.draw_text('ПРАВИЛЬНО',500,400,ar.color.GREEN,30)
                self.fon -= 2
            if key == ar.key.R:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.T:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
            if key == ar.key.Y:
                ar.draw_text('ОШИБКА',500,400,ar.color.RED,30)
        pass 
     
# основная функция
def main():
    # присвоение к переменной основнго класса
    window = Mygame(WIDTH,HEIGHT,TITLE)

    window.setup()

    ar.run()

# вызов функции 
main()