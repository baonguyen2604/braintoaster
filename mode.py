import pygame
import sys
import random
from helper import *
from pygame import *
from random import *

BLUE = (69, 142, 255)
RED = (251, 57, 88)
WHITE = (222, 209, 193)
GREEN = (109, 201, 147)
BROWN = (155, 105, 84)


class Mode:

    def __init__(self):
        return


class MathGame(Mode):
    math_string = ''
    result = ''
    correct_answer_rect = pygame.Rect(100, 700, 100, 100)
    wrong_answer_rect = pygame.Rect(350, 700, 100, 100)
    fake_result = ''

    # implement init later
    def __init__(self):
        self.math_string = self._get_string()
        self.result = self._calculate_result()
        random_rect = randrange(0, 2)

        if random_rect == 0:
            self.correct_answer_rect, self.wrong_answer_rect = self.wrong_answer_rect, self.correct_answer_rect

    def play_game(self, screen, health):

        cur_health = health
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.correct_answer_rect.collidepoint(mousex, mousey):
                        return (True, cur_health)
                    elif self.wrong_answer_rect.collidepoint(mousex, mousey):
                        return (False, cur_health)
                else: self.draw(screen, cur_health)
            self.draw(screen, health)

    def set_up_game(self):
        self.math_string = self._get_string()
        self.result = self._calculate_result()
        random_rect = randrange(0, 2)
        rand_diff = randint(-10, 11)
        if rand_diff == 0:
            rand_diff += 1
        self.fake_result = self.result + rand_diff

        if random_rect == 0:
            self.correct_answer_rect, self.wrong_answer_rect = self.wrong_answer_rect, self.correct_answer_rect

        #self.draw(screen, health)

    def draw(self, screen, health):
        screen.fill((69, 187, 255))
        # draw math string
        font_blit(screen, (250, 300), 60, self.math_string, RED)

        # draw answers
        pygame.draw.rect(screen, WHITE, self.correct_answer_rect)

        # add text to button
        correct_answer_rect = (self.correct_answer_rect.left + self.correct_answer_rect.width/2,
                               self.correct_answer_rect.top + self.correct_answer_rect.height/2)
        font_blit(screen, correct_answer_rect, 30, str(self.result), BROWN)

        pygame.draw.rect(screen, WHITE, self.wrong_answer_rect)

        wrong_answer_rect = (self.wrong_answer_rect.left + self.wrong_answer_rect.width/2,
                             self.wrong_answer_rect.top + self.wrong_answer_rect.height/2)
        font_blit(screen, wrong_answer_rect, 30, str(self.fake_result), GREEN)

        # draw health
        drawHealth(screen, health)
        # draw clock
        #drawTime(clock, screen)

        wrong_answer_rect = (self.wrong_answer_rect.left + self.wrong_answer_rect.width/2,
                             self.wrong_answer_rect.top + self.wrong_answer_rect.height/2)
        font_blit(screen, wrong_answer_rect, 30, str(self.fake_result), BROWN)

        pygame.display.update()

    def _calculate_result(self):
        if len(self.math_string) < 7:
            print("Error: not a valid math_string")
        index = 0
        temp = []
        check = 0

        while check < len(self.math_string):
            if self.math_string[check] == ' ':
                len_of_num = check-index
                if len_of_num > 0:
                    temp.append(self.math_string[index:check])
                else:
                    print("Error: not a valid operator or operand")
                index = check+1
            check += 1

        if temp[1] == "+":
            return int(temp[0]) + int(temp[2])
        elif temp[1] == "-":
            return int(temp[0]) - int(temp[2])
        elif temp[1] == "*":
            return int(temp[0]) * int(temp[2])
        else:
            return int(temp[0]) / int(temp[2])

    def _get_string(self):
        self.math_string = ""
        x = randrange(0, 10)
        y = randrange(1, 10)
        opran = randrange(0, 4)

        if opran == 1:
            self.math_string += str(x) + " + " + str(y) + " = "
        elif opran == 2:
            self.math_string += str(x) + " - " + str(y) + " = "
        elif opran == 3:
            self.math_string += str(x) + " * " + str(y) + " = "
        else:
            self.math_string += str(x) + " / " + str(y) + " = "
        return self.math_string


class ColorGame(Mode):

    COLOR = [('RED', 251, 57, 88),
             ('GREEN', 109, 201, 147),
             ('BLUE', 69, 142, 255),
             ('PURPLE', 255, 0, 255),
             ('YELLOW', 255, 200, 56),
             ('BROWN', 155, 105, 84),
             ('BLACK', 0, 0, 0)]
    FOUR_COLOR = sample(COLOR, 4)
    ANSWER = randint(0, 3)
    ANSWER_COLOR = randint(0, 3)

    def __init__(self):
        super.__init__

    def set_up_game(self):
        self.FOUR_COLOR = sample(self.COLOR, 4)
        self.ANSWER = randint(0, 3)
        self.ANSWER_COLOR = randint(0, 3)

    # implement init later
    def play_game(self):
        mousex = 0
        mousey = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.ANSWER == 0:
                        if 10 < mousex < 245 and 380 < mousey < 680:
                            return True
                        else:
                            return False
                    elif self.ANSWER == 1:
                        if 10 < mousex < 245 and 690 < mousey < 990:
                            return True
                        else:
                            return False
                    elif self.ANSWER == 2:
                        if 255 < mousex < 490 and 380 < mousey < 680:
                            return True
                        else:
                            return False
                    elif self.ANSWER == 3:
                        if 255 < mousex < 490 and 690 < mousey < 990:
                            return True
                        else:
                            return False

    def draw(self, screen):
        screen.fill((222, 209, 193))
        font_blit(screen, (250, 280), 80, self.FOUR_COLOR[self.ANSWER][0], (self.FOUR_COLOR[self.ANSWER_COLOR][1],
                                                                            self.FOUR_COLOR[self.ANSWER_COLOR][2],
                                                                            self.FOUR_COLOR[self.ANSWER_COLOR][3]))
        pygame.draw.rect(screen, (self.FOUR_COLOR[0][1],
                                  self.FOUR_COLOR[0][2],
                                  self.FOUR_COLOR[0][3]), (10, 380, 235, 300))
        pygame.draw.rect(screen, (self.FOUR_COLOR[1][1],
                                  self.FOUR_COLOR[1][2],
                                  self.FOUR_COLOR[1][3]), (10, 690, 235, 300))
        pygame.draw.rect(screen, (self.FOUR_COLOR[2][1],
                                  self.FOUR_COLOR[2][2],
                                  self.FOUR_COLOR[2][3]), (255, 380, 235, 300))
        pygame.draw.rect(screen, (self.FOUR_COLOR[3][1],
                                  self.FOUR_COLOR[3][2],
                                  self.FOUR_COLOR[3][3]), (255, 690, 235, 300))

        pygame.display.update()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000
class OperatorGame(Mode):

    missing_string = ''
    result = ''

    plus_rec = pygame.Rect(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2, 150, 150)
    minus_rec = pygame.Rect(SCREEN_WIDTH - (SCREEN_WIDTH/5) - 140, SCREEN_HEIGHT/2, 150, 150)
    multiply_rec = pygame.Rect(SCREEN_WIDTH / 5, SCREEN_HEIGHT/2+160, 150, 150)
    divide_rec = pygame.Rect(SCREEN_WIDTH - (SCREEN_WIDTH/5) - 140, SCREEN_HEIGHT/2+160, 150, 150)
    ope = ["+", "-", "*", "/"]

    def __init__(self):
        self.missing_string = self._get_string()
        self.result = self._get_operator()
        self.result_index = self.ope.index(self.result)

    def play_game(self, screen, health):
        cur_health = health
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.plus_rec.collidepoint(mousex, mousey):
                        if self.result_index == 0:
                            return True, cur_health
                        else:
                            return False,cur_health
                    if self.minus_rec.collidepoint(mousex, mousey):
                        if self.result_index == 1:
                            return True, cur_health
                        else:
                            return False, cur_health
                    if self.multiply_rec.collidepoint(mousex, mousey):
                        if self.result_index == 2:
                            return True, cur_health
                        else:
                            return False, cur_health
                    if self.divide_rec.collidepoint(mousex, mousey):
                        if self.result_index == 3:
                            return True, cur_health
                        else:
                            return False, cur_health

                else: self.draw(screen, cur_health)
            self.draw(screen, health)

    def set_up_game(self):
        self.missing_string = self._get_string()
        self.result = self._get_operator()

    def draw(self, screen, health):
        screen.fill((69, 187, 255))
        # draw math string
        font_blit(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3/10), 60, self._update_missing_string(self.missing_string), RED)

        # draw answers
        pygame.draw.rect(screen, WHITE, self.plus_rec)
        pygame.draw.rect(screen, WHITE, self.minus_rec)
        pygame.draw.rect(screen, WHITE, self.multiply_rec)
        pygame.draw.rect(screen, WHITE, self.divide_rec)

        # add text to button
        plus_rect = (self.plus_rec.left + self.plus_rec.width/2,
                               self.plus_rec.top + self.plus_rec.height/2)
        font_blit(screen, plus_rect, 30, "+", BROWN)

        minus_rect = (self.minus_rec.left + self.minus_rec.width / 2,
                     self.minus_rec.top + self.minus_rec.height / 2)
        font_blit(screen, minus_rect, 30, "-", BROWN)

        mul_rect = (self.multiply_rec.left + self.multiply_rec.width / 2,
                     self.multiply_rec.top + self.multiply_rec.height / 2)
        font_blit(screen, mul_rect, 30, "*", BROWN)

        divide_rect = (self.divide_rec.left + self.divide_rec.width / 2,
                     self.divide_rec.top + self.divide_rec.height / 2)
        font_blit(screen, divide_rect, 30, "/", BROWN)

        # draw health
        drawHealth(screen, health)
        # draw clock
        # drawTime(clock, screen)

        pygame.display.update()

    def _update_missing_string(self, string):
        if len(self.missing_string) < 9:
            print("Error: not a valid missing_string")
        temp = string
        operator_list = ["+", "-", "*", "/"]
        for chr in string:
            if chr in operator_list:
                temp = temp.replace(chr, "  ")
                return temp
        return temp

    def _get_operator(self):
        if len(self.missing_string) < 9:
            print("Error: not a valid missing_string")

        operator_list = ["+", "-", "*", "/"]
        for chr in self.missing_string:
            if chr in operator_list:
                return chr
        return -1

    def _get_string(self):
        self.missing_string = ""

        x = randrange(1, 10)
        y = randrange(1, 10)
        opran = randrange(0, 4)

        if opran == 1:
            res = x + y
            self.missing_string += str(x) + " + " + str(y) + " = " + str(res)
        elif opran == 2:
            res = x - y
            self.missing_string += str(x) + " - " + str(y) + " = " + str(res)
        elif opran == 3:
            res = x*y
            self.missing_string += str(x) + " * " + str(y) + " = " + str(res)
        else:
            res = x/y
            self.missing_string += str(x) + " / " + str(y) + " = " + str(res)
        return self.missing_string


