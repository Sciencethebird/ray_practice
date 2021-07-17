# ray_practice
2021, Ray learning for DeepRacer and tt-racer

Ray 
===
- [Ray + Gym example](https://docs.ray.io/en/master/ray-overview/index.html)

OpenAI Gym
===
- [OpenAI official doc](https://gym.openai.com/docs/)

    Basic Structure of Custom Environment
    ---
    ```python
    class MyCustomEnv(gym.Env):
        def __init__(self, config):
        
            # environment value init....
    
            # observation space definition...
    
        def reset(self) -> "initial observation":
        
            # reset your environment....
    
            return initial_observation
    
        def step(self, action) -> "observation, reward, done, info":
        
            # code for stepping in your environment
    
            return observation, reward, done, info
    ```
