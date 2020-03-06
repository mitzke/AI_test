import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import Macke_neu as macke


class AItest(gym.Env):
    metadata = {'render.modes': ['human']}
    WUERFELN = 1
    AUFHOEREN = 2
    def __init__(self):
        n_actions = 2
        self.points, self.wurf_neu = macke.wuerfeln(5)
        self.action_space = spaces.Discrete(n_actions)
        # The observation will be the current points
        self.observation_space = spaces.Box(low=0, high=1000
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
        reward = self.points

        # Optionally we can pass additional info, we are not using that for now
        info = {}

        return self.points reward, done, info


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

