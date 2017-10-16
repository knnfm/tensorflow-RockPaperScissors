import os
import numpy as np


class CatchBall:
    def __init__(self):
        # parameters
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        # Rock, Paper, Scissors
        self.enable_actions = (0, 1, 2)
        # variables
        self.reset()

    def update(self, action):
        """
        action:
            0: Rock
            1: Paper
            2: Scissors
        """
        print action

        if action == 0:
            if self.enemy_card[0][0] == 1:
                self.reward = 0
            elif self.enemy_card[0][1] == 1:
                self.reward = -1
            else:
                self.reward = 1
        elif action == 1:
            if self.enemy_card[0][0] == 1:
                self.reward = 1
            elif self.enemy_card[0][1] == 1:
                self.reward = 0
            else:
                self.reward = -1
        else:
            if self.enemy_card[0][0] == 1:
                self.reward = -1
            elif self.enemy_card[0][1] == 1:
                self.reward = 1
            else:
                self.reward = 0

    def observe(self):
        return self.enemy_card, self.reward

    def execute_action(self, action):
        self.update(action)

    def reset(self):
        # reset enemy
        self.enemy_card = np.zeros((1, 3))
        self.enemy_card[0][np.random.randint(3)] = 1
        # reset other variables
        self.reward = 0

    def set_card(self, action):
        self.enemy_card = np.zeros((1, 3))
        self.enemy_card[0][int(action)] = 1
