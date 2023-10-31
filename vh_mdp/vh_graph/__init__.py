from gym.envs.registration import register
from vh_graph.envs.vh_env import VhGraphEnv

register(
    id='vh_graph-v0',
    entry_point='vh_graph.envs:VhGraphEnv',
)
