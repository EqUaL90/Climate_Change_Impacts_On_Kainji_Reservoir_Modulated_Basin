Being the code for the submitted manuscript titled "Hybrid Quantile Delta - Deep Learning Bias Correction Technique for Enhancing Climate Risk Assessment in a Reservoir-Modulated Basin"

Run the main_pipeline.py script after obtaining the right data. Our data have been removed for privacy reasons


Residual-based QDM-LSTM Hybrid Bias Correction Technique for CMIP6 Climate Projections in Reservoir-Modulated Basins
Overview

This repository provides the main workflow used to develop a two-stage hybrid bias-correction framework (QDM–LSTM) for climate projections. The framework combines Quantile Delta Mapping (QDM) with a Long Short-Term Memory (LSTM) neural network to correct both distributional bias and residual temporal structure in CMIP6 simulations.

The method was developed to improve the reliability of precipitation and temperature projections used for hydroclimatic impact assessment in data-sparse regions.

The workflow includes:

Dataset preprocessing and harmonization

Spatial regridding and basin extraction

QDM bias correction

Residual error computation

LSTM-based residual learning

Bayesian hyperparameter optimization

Future climate projection correction

Performance evaluation and visualization

The approach ensures that climate change signals are preserved (via QDM) while temporal biases are corrected (via LSTM residual learning) even with few GCMs (typical of data cost / data scarcity problems in developing countries) as we focus only on individual GCM contributions and not mean ensemble which may introduce more randomness and heterogeneity.
