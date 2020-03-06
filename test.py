import gym
import AI_test
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
#from stable_baselines.common.env_checker import check_env


env = gym.make('AI_test:Ai-v0')
#check_env(env, warn=True)

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=10)

obs = env.reset()
for i in range(10):
    action, _states = model.predict(obs)
    rewards, dones, info = env.step(action)
    env.render()