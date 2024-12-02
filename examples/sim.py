import gymnasium as gym
import gym_aloha
import numpy as np
import imageio

print("in here")

# Create the ALOHA environment
env = gym.make("gym_aloha/AlohaInsertion-v0", render_mode="rgb_array")



observation, info = env.reset()
frames = []

print("in here")
# Run simulation for 1000 steps
for _ in range(1000):
    action = env.action_space.sample()  # Random actions
    observation, reward, terminated, truncated, info = env.step(action)
    frame = env.render()
    frames.append(frame)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()

# Save the simulation as a video
imageio.mimsave("simulation.mp4", np.stack(frames), fps=25)