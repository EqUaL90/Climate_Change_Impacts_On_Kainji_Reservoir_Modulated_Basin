import numpy as np

def kling_gupta_efficiency(sim, obs):

    r = np.corrcoef(sim,obs)[0,1]

    alpha = np.std(sim)/np.std(obs)

    beta = np.mean(sim)/np.mean(obs)

    kge = 1 - np.sqrt((r-1)**2 + (alpha-1)**2 + (beta-1)**2)

    return kge