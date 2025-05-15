import random
from turtle import Turtle

RANGE = 250

def generate_food():

    food = Turtle('circle')
    food.color('white')
    food.penup()
    x_cor = get_num(-RANGE, RANGE, 20)
    y_cor = get_num(-RANGE, RANGE, 20)

    food.goto(x=x_cor, y=y_cor)
    return food

def get_num(a, b, x):
    if not a % x:
        return random.choice(range(a, b, x))
    else:
        return random.choice(range(a + x - (a%x), b, x))

ACCOUNTED_FOR_SPACE = 280
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')

        self.refresh()

    def refresh(self):
        random_x = random.randint(-ACCOUNTED_FOR_SPACE, ACCOUNTED_FOR_SPACE)
        random_y = random.randint(-ACCOUNTED_FOR_SPACE, ACCOUNTED_FOR_SPACE)
        self.color(
            random.choice([
                'blue', 'red', 'purple', 'green', 'orange', 'yellow'
            ])
        )
        self.goto(x=random_x, y=random_y)


