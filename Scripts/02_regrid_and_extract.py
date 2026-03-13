import xarray as xr
import xesmf as xe

def regrid_dataset(source_ds, target_ds):
    regridder = xe.Regridder(source_ds, target_ds, "bilinear")
    return regridder(source_ds)

def extract_basin(ds, shapefile):
    import rioxarray
    basin = ds.rio.clip(shapefile.geometry)
    return basin