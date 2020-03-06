import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import Macke_neu as macke
from stable_baselines.common.env_checker import check_env


class AItest(gym.Env):
    metadata = {'render.modes': ['human']}
    WUERFELN = 1
    AUFHOEREN = 0
    def __init__(self):
        n_actions = 2
        self.points = 0
        self.reward = self.points
        self.wurf_neu = [0,0,0,0,0]
        self.action_space = spaces.Discrete(n_actions)
        # The observation will be the current points
        self.observation_space = spaces.Box(low=0, high=1000,
                                        shape=(1,), dtype=np.float32)


    def step(self, action):
        if action == self.WUERFELN:
          self.points, self.wurf_neu = macke.weiterwuerfeln(len(self.wurf_neu))
        elif action == self.AUFHOEREN:
          print ("Aufhören")
        else:
          raise ValueError("Received invalid action={} which is not part of the action space".format(action))

        # Are we at the left of the grid?
        done = bool(self.points == 1000)
        
        # Null reward everywhere except when reaching the goal (left of the grid)
        if self. points > 0:
            self.reward += self.points
        else:
            self.reward = 0

        # Optionally we can pass additional info, we are not using that for now
        info = {}
        reward = self.reward
        return np.array([self.points]).astype(np.float32), reward, done, info


    def reset(self):
        self.points = 0
        return np.array([self.points]).astype(np.float32)


    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass

env = AItest()

obs = env.reset()
env.render()

print(env.observation_space)
print(env.action_space)
print(env.action_space.sample())

WUERFELN = 1
# Hardcoded best agent: always go left!
n_steps = 5
for step in range(n_steps):
  print("Step {}".format(step + 1))
  obs, reward, done, info = env.step(WUERFELN)
  print('obs=', obs, 'reward=', reward, 'done=', done)
  env.render()
  if done:
    print("Goal reached!", "reward=", reward)
    break