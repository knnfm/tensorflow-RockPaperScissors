from __future__ import division

import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from catch_ball import CatchBall
from dqn_agent import DQNAgent


def init():
    img.set_array(state_t_1)
    plt.axis("off")
    return img


def get_hand_name(hand):
    if hand == 0:
        return "Rock"
    elif hand == 1:
        return "Papper"
    else:
        return "Scissors"

def get_hand_number(hand_list):
    if hand_list[0][0] == 1:
        return 0
    elif hand_list[0][1] == 1:
        return 1
    else:
        return 2

def print_log(cpu_hand, myself_hand, reward):
    log = []
    log.append("CPU:")
    log.append(get_hand_name(cpu_hand))
    log.append(" ")
    log.append("MySelf:")
    log.append(get_hand_name(myself_hand))

    if reward == 0:
        print "CPU EVEN " + "".join(log)
    elif reward == 1:
        print "CPU WIN " + "".join(log)
    else:
        print "CPU LOSE " + "".join(log)


if __name__ == "__main__":
        # args
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_path")
    parser.add_argument("-a", "--action")
    args = parser.parse_args()

    # environmet, agent
    env = CatchBall()
    agent = DQNAgent(env.enable_actions, env.name)
    agent.load_model(args.model_path)
    env.set_card(args.action)
    state_t, reward_t = env.observe()

    # variables
    action_t = agent.select_action(state_t, 0.0)
    env.execute_action(action_t)
    state_t, reward_t = env.observe()

    print_log(int(action_t), get_hand_number(state_t), reward_t)
