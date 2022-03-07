# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 20/21 - Snake Game

from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self, width, height):
        super().__init__()
        #self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(0, height/2 - 0.05*height)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write('Score: ' + str(self.score), font=FONT, align=ALIGN)
        self.hideturtle()

    def add_point(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0 ,0)
        self.write('GAME OVER', font=FONT, align=ALIGN)