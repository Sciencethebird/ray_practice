# this example is modified from https://docs.ray.io/en/master/ray-overview/index.html
import gym
from gym.spaces import Discrete, Box
from ray import tune

'''
This is a simple example for building your own custom gym environment.
The goal is training a RL network with ray to walk from 0 to "corridor_length"
'''
'''
See each function definition and their return values here https://gym.openai.com/docs/#observations
'''
class SimpleCorridor(gym.Env):
    def __init__(self, config):
        print(config["print_message"])
        self.end_pos = config["corridor_length"] # from env_config
        self.cur_pos = 0
        self.action_space = Discrete(2)
        self.observation_space = Box(0.0, self.end_pos, shape=(1, ))

    def reset(self):
        # reset environment after every episode
        self.cur_pos = 0
        return [self.cur_pos]

    def step(self, action) -> "obs, reward, done, info":

        # return value:
        #   "obs", observation of the enviroment
        #   "reward", the reward from current step
        #   "done", see if the enviroment reaches terminal state
        #   "info"

        if action == 0 and self.cur_pos > 0:
            self.cur_pos -= 1
        elif action == 1:
            self.cur_pos += 1
        print(f"current position: {self.cur_pos}")
        done = self.cur_pos >= self.end_pos
        return [self.cur_pos], 1 if done else 0, done, {}

tune.run(
    "PPO",
    config={
        "env": SimpleCorridor,
        "num_workers": 4,
        "env_config": {"corridor_length": 5, "print_message": "Hello World!"}})