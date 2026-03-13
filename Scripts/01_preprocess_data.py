import xarray as xr
import pandas as pd

def load_dataset(path):
    ds = xr.open_dataset(path)
    return ds

def convert_units(ds, variable):
    if variable == "pr":
        ds[variable] = ds[variable] * 86400
    return ds

def temporal_subset(ds, start, end):
    return ds.sel(time=slice(start, end))

def save_processed(ds, path):
    ds.to_netcdf(path)