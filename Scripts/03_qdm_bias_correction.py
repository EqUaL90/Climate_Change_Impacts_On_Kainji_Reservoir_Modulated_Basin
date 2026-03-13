import numpy as np
from scipy.stats import rankdata

def empirical_cdf(data):
    ranks = rankdata(data, method='average')
    return ranks / (len(data) + 1)

def quantile_delta_mapping(obs, gcm_hist, gcm_future):

    F_obs = empirical_cdf(obs)
    F_gcm = empirical_cdf(gcm_hist)

    corrected = np.interp(
        empirical_cdf(gcm_future),
        F_gcm,
        obs
    )

    return corrected