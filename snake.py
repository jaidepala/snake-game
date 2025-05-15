from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

def create_segment():
    snake = Turtle(shape='square')
    snake.color('white')
    snake.penup()
    return snake

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake(3)
        self.head = self.segments[0]

    def add_segment(self):
        # new_snake = Turtle(shape='square')
        new_snake = Turtle(shape='square')
        new_snake.color('white')
        new_snake.penup()
        last_segment = self.segments[len(self.segments) - 1]
        new_snake.goto(x=last_segment.xcor, y=last_segment.ycor)
        self.segments.append(new_snake)

    """Creates a snake of size n"""
    def create_snake(self, size_of_snake):
        for num in range(0, size_of_snake):
            snake = create_segment()
            snake.goto(x=-20 * num, y=0)
            self.segments.append(snake)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    """Moves the snake forward"""
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def is_snake_out_of_bounds(self):
        end_cor = 280
        is_x_out_of_bounds = -end_cor > self.head.xcor() or self.head.xcor() > end_cor
        is_y_out_of_bounds = -end_cor > self.head.ycor() or self.head.ycor() > end_cor

        return is_x_out_of_bounds or is_y_out_of_bounds

    def is_tail_touched(self):
        for seg_num in range(1, len(self.segments) - 1):
            snake_body = self.segments[seg_num]
            if self.head.distance(snake_body) < 10:
                print(self.head, snake_body)
                return True

        return False

