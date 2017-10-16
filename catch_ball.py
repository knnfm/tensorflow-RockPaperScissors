import os
import numpy as np


class CatchBall:
    def __init__(self):
        # parameters
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        self.enable_actions = (0, 1, 2)
        self.reset()

    def get_hand_name(self, hand):
        if hand == 0:
            return "Rock"
        elif hand == 1:
            return "Papper"
        else:
            return "Scissors"

    def get_hand_number(self, hand_list):
        if hand_list[0][0] == 1:
            return 0
        elif hand_list[0][1] == 1:
            return 1
        else:
            return 2

    def print_result(self, ai_hand, challenger_hand, reward):
        log = []
        log.append("AI:")
        log.append(self.get_hand_name(ai_hand))
        log.append(" ")
        log.append("Challenger:")
        log.append(self.get_hand_name(challenger_hand))

        if reward == 0:
            print "AI EVEN " + "".join(log)
        elif reward == 1:
            print "AI WIN " + "".join(log)
        else:
            print "AI LOSE " + "".join(log)

    def update(self, action):
        t_action = self.get_hand_number(self.enemy_card)

        if (action == t_action):
            self.reward = 0
        elif (action == 0 and t_action == 2) or (action == 1 and t_action == 0) or (action == 2 and t_action == 1):
            self.reward = 1
        else:
            self.reward = -1

        self.print_result(action, t_action, self.reward)

    def observe(self):
        return self.enemy_card, self.reward

    def execute_action(self, action):
        self.update(action)

    def reset(self):
        self.enemy_card = np.zeros((1, 3))
        self.enemy_card[0][np.random.randint(3)] = 1
        self.reward = 0

    def set_card(self, action):
        self.enemy_card = np.zeros((1, 3))
        self.enemy_card[0][int(action)] = 1
