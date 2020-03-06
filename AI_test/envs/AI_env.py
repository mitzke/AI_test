import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import Macke_neu as macke


class AItest(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # Actions of the format Buy x%, Sell x%, Hold, etc.
        self.action_space = spaces.Box(
         low=np.array([0, 0]), high=np.array([2, 1]), dtype=np.float16)    # Prices contains the OHCL values for the last five prices
        self.observation_space = spaces.Box(
         low=0, high=1, shape=(6, 6), dtype=np.float16)


    def step(self, action):
        self.wurfpunkte, self.wurf_rest = macke.wuerfeln(5)
        self.Gesamtpunkte += self.wurfpunkte
  
        reward = self.Gesamtpunkte
        done = self.wurfpunkte <= 0  
        return  reward, done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.wurfpunkte = 0
        self.Gesamtpunkte = 0
        self.Wurfzahl = 1
        self.Zwischenstand = 0
        self.wurf = []
        done = True
  
        return  done

    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass

