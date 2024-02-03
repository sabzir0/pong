from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import NumericProperty,ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PongBall(Widget):
    velocity_x = NumericProperty(5)
    velocity_y = NumericProperty(5)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)

    def update(self, dt):
        self.ball.move()


        if self.ball.x < self.x or self.ball.right > self.right:
            self.ball.velocity_x *= -1
        
        if self.ball.y < self.y or self.ball.top > self.top:
            self.ball.velocity_y *= -1
            


class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1/60)
        return game

PongApp().run()