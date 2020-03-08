import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import random
import Macke_neu as macke
from stable_baselines.common.env_checker import check_env
from stable_baselines import DQN, PPO2, A2C, ACKTR
from stable_baselines.bench import Monitor
from stable_baselines.common.vec_env import DummyVecEnv

rundenanzahl = np.array([0])

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
                                        shape=(3,), dtype=np.float32)


    def step(self, action):
        if action == self.WUERFELN:
          self.geschrieben = 0
          #self.rundennummer +=1
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
              #self.rundennummer =1
              self.wurfnummer =1
              self.wurfpunkte = 0
              self.wurf_neu = [0,0,0,0,0]
              
        elif action == self.AUFHOEREN:
          if self.geschrieben == 1:
            #self.gesamtpunkte -= 100
            self.rundennummer +=1
            print ("doppelt geschrieben")
          else:
            self.gesamtpunkte += self.rundenpunkte
            self.rundenpunkte = 0
            self.wurfpunkte = 0
            self.rundennummer += 1
            self.wurfnummer = 1
            self.wurf_neu = [0,0,0,0,0]
            self.geschrieben = 1
            #print ("Aufhören, Gesamtpunkte =", self.gesamtpunkte, "Rundennummer:", self.rundennummer)
        else:
          raise ValueError("Received invalid action={} which is not part of the action space".format(action))

        # Are we at the left of the grid?
        done = bool(self.gesamtpunkte > 5000)
        if done:
          global rundenanzahl
          print ("gewonnen nach ", self.rundennummer, "Runden")
          rundenanzahl = np.append(rundenanzahl, self.rundennummer)
          self.rundennummer = 1
        
        # Null reward everywhere except when reaching the goal (left of the grid)

        # Optionally we can pass additional info, we are not using that for now
        info = {}
        reward = -self.rundennummer
        return np.array([self.wurfpunkte, len(self.wurf_neu), self.rundenpunkte]).astype(np.float32), reward, done, info


    def reset(self):
        self.wurfpunkte = 0
        self.wurfnummer = 1
        self.rundennummer = 1
        self.rundenpunkte = 0
        self.gesamtpunkte = 0
        self.wurf_neu = [0,0,0,0,0]
        self.geschrieben = 0
        return np.array([self.wurfpunkte]).astype(np.float32)


    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass


env = AItest()
env = Monitor(env, filename=None, allow_early_resets=True)
env = DummyVecEnv([lambda: env])
#Train the agent and save
#model = ACKTR('MlpPolicy', env, verbose=1).learn(20000)
#model.save('Macke_AI')
# run with saved agent
model =ACKTR.load('Macke_AI')

## Test the trained agent
#obs = env.reset()
#n_steps = 100
#for step in range(n_steps):
#  action, _ = model.predict(obs, deterministic=True)
#  #print("Step {}".format(step + 1))
#  #print("Action: ", action)
#  obs, reward, done, info = env.step(action)
#  #print('obs=', obs, 'reward=', reward, 'done=', done)
#  env.render()
#  if done:
#    # Note that the VecEnv resets automatically
#    # when a done signal is encountered
#    print("Goal rreached!", "reward=", reward)
#    break

obs = env.reset()
n_games = 100
spielnummer = 1
while spielnummer < n_games:
  action, _ = model.predict(obs, deterministic=True)
  obs, reward, done, info = env.step(action)
  #print (reward)
  env.render()
  if done:
    print("Spiel No ", spielnummer)
    spielnummer +=1
    #rundenanzahl = np.append(rundenanzahl, -reward)

print (rundenanzahl, "mittelwert:", rundenanzahl.mean())