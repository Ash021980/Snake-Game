from turtle import Turtle
import random


class Food(Turtle):
    """ Creates and refreshes the food objects for the snake to eat. """

    def __init__(self) -> None:
        """ Initialize the food object """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def __str__(self) -> str:
        return "Food will appear in random locations on the board, after a piece is eaten."

    def refresh(self) -> None:
        """
            Creates a new food object in a random location after the snake
            has eaten the previous piece of food and has not died.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
