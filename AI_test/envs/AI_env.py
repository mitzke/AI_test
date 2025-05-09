import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import Macke_neu as macke



class AItest(gym.Env):
    metadata = {'render.modes': ['human']}
    WUERFELN = 1
    AUFHOEREN = 0
    def __init__(self):
        n_actions = 2
        self.wurfpunkte = 0
        self.wurfnummer = 1
        self.rundennummer = 1
        self.rundenpunkte = 0
        self.gesamtpunkte = 0
        self.wurf_neu = [0,0,0,0,0]
        self.geschrieben = 0
        self.action_space = spaces.Discrete(n_actions)
        # The observation will be the current points
        self.observation_space = spaces.Box(low=0, high=1000,
                                        shape=(1,), dtype=np.float32)


    def step(self, action):
        if action == self.WUERFELN:
          self.geschrieben = 0
          if len(self.wurf_neu) == 0:
            self.wurfpunkte, self.wurf_neu = macke.weiterwuerfeln(5)
            self.wurfnummer +=1
            if self.wurfpunkte >0:
              self.rundenpunkte += self.wurfpunkte
            else:
              self.rundenpunkte += 1000
          else:
            self.wurfpunkte, self.wurf_neu = macke.weiterwuerfeln(len(self.wurf_neu))
            self.wurfnummer +=1
            if self.wurfpunkte >0:
              self.rundenpunkte += self.wurfpunkte
            else:
              self.rundenpunkte = 0
              self.rundennummer =1
              self.wurfnummer =1
              self.wurfpunkte = 0
              self.wurf_neu = [0,0,0,0,0]
              
        elif action == self.AUFHOEREN:
          if self.geschrieben == 1:
            self.gesamtpunkte -= 100
          else:
            self.gesamtpunkte += self.rundenpunkte
            self.rundenpunkte = 0
            self.wurfpunkte = 0
            self.rundennummer += 1
            self.wurfnummer = 1
            self.wurf_neu = [0,0,0,0,0]
            self.geschrieben = 1
            #print ("Aufhören, Gesamtpunkte =", self.gesamtpunkte)
        else:
          raise ValueError("Received invalid action={} which is not part of the action space".format(action))

        # Are we at the left of the grid?
        done = bool(self.gesamtpunkte > 5000)
        if done:
          print ("gewonnen nach ", self.rundennummer, "Runden")
        
        # Null reward everywhere except when reaching the goal (left of the grid)

        # Optionally we can pass additional info, we are not using that for now
        info = {}
        reward = self.gesamtpunkte
        return np.array([self.wurfpunkte]).astype(np.float32), reward, done, info


    def reset(self):
        self.wurfpunkte = 0
        self.wurfnummer = 1
        self.rundennummer = 1
        self.rundenpunkte = 0
        self.gesamtpunkte = 0
        return np.array([self.wurfpunkte]).astype(np.float32)


    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass