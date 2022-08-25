from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
START_POSITIONS = [(20, 0) , (0, 0), (-20, 0)]


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.extend(position)

    def extend(self, position):
        part = Turtle(shape="square")
        part.resizemode("user")
        part.shapesize(0.9, 0.9)
        part.color(87, 166, 53)
        part.penup()
        part.speed("fastest")
        part.goto(position)
        self.body.append(part)

    def tail_position(self):
        return self.body[len(self.body) - 1].position()

    def move(self):
        # starting from the end of the snake, each part moves to the position of the part before him (except the head)
        for part in range(len(self.body) - 1, 0, -1):
            position_ahead = self.body[part - 1].position()
            self.body[part].goto(position_ahead)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def collided(self):
        for segment in self.body[1 : ]:
            distance = self.head.distance(segment)
            if distance < 10:
                return True

        return False




