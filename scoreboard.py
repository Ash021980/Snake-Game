from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """ Provides the scoreboard to keep track of the player's score."""
    
    def __init__(self) -> None:
        """ Initialize the scoreboard object and sets its position on the screen."""
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 275)
        self.update_scoreboard()

    def __str__(self) -> str:
        return "Scoreboard to keep track of the user's score."

    def update_scoreboard(self) -> None:
        """ Updates the scoreboard after successfully eating the food."""

        self.clear()
        self.write(arg=f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        """
            Increases the score when the snake is successful at eating the
            food without dying.
        """

        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self) -> None:
        """ Resets the scoreboard to reflect the high score. """

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
