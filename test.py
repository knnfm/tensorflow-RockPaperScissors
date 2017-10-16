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

def print_log(env, cpu_hand, myself_hand, reward):
    log = []
    log.append("CPU:")
    log.append(env.get_hand_name(cpu_hand))
    log.append(" ")
    log.append("MySelf:")
    log.append(env.get_hand_name(myself_hand))

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

    print_log(env, int(action_t), env.get_hand_number(state_t), reward_t)
