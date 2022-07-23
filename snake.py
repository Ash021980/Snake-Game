from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
        Creates the Snake and sets the behavior of the snake.  Including the snakes
        movement and adding the additional segments to the snake when the snake successfully
        eats a piece of food.
    """

    def __init__(self) -> None:
        """
            Initializes the snake default settings.  The head of the snake starts with a default
            position of (0,0).  The distance the snake will move defaults to 20.
        """

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def __str__(self) -> str:
        return f"Snake(Starting position={STARTING_POSITIONS[0]}, Starting segment length= 3.)"

    def create_snake(self) -> None:
        """
            Initializes the snake object with three square turtles with the default square color
            being white.  Increments the placement of the squares to create the snake.
        """

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple) -> None:
        """ Creates a new snake segment."""

        segment = Turtle(shape="square")
        segment.color("blue")
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self) -> None:
        """ Adds the new segment to the snake when the snake eats the food."""

        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        """
            Moves snake across the screen by having the last square(tail)
            move to the present location of the square in front of it.
            Repeats the process for the length of the snake.
        """

        for seg_num in range(len(self.segments) - 1, 0, -1):
            x, y = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(x, y)
        self.head.fd(MOVE_DISTANCE)

    def up(self) -> None:
        """
            Turns the snake up(north).  Keeps the snake from being able to
            move down while the snake is moving up.
        """

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """
            Turns the snake down(south).  Keeps the snake from being able to
            move up while the snake is moving down.
        """

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """
            Turns the snake left(west).  Keeps the snake from being able to
            move right while the snake is moving left.
        """

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """
            Turns the snake right(east).  Keeps the snake from being able to
            move left while the snake is moving right.
        """

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        """ Resets the snake back to its default length and position"""

        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

