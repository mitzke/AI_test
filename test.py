import gym
import AI_test
from stable_baselines.common.env_checker import check_env
from stable_baselines import DQN, PPO2, A2C, ACKTR
from stable_baselines.bench import Monitor
from stable_baselines.common.vec_env import DummyVecEnv


env = gym.make('AI_test:Ai-v0')
env = Monitor(env, filename=None, allow_early_resets=True)
env = DummyVecEnv([lambda: env])
model = ACKTR('MlpPolicy', env, verbose=1).learn(10000)

# Test the trained agent
obs = env.reset()
n_steps = 100
for step in range(n_steps):
  action, _ = model.predict(obs, deterministic=True)
  print("Step {}".format(step + 1))
  print("Action: ", action)
  obs, reward, done, info = env.step(action)
  print('obs=', obs, 'reward=', reward, 'done=', done)
  env.render()
  if done:
    # Note that the VecEnv resets automatically
    # when a done signal is encountered
    print("Goal reached!", "reward=", reward)
    break