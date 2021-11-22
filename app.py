import streamlit as st
import xarray as xr
import pandas as pd
import numpy as np
import itertools
from utils.read_data_utils import read_is2_data
from utils.plotting_utils import interactiveArcticMaps

# Plotting dependencies
import cartopy.crs as ccrs
from textwrap import wrap
import hvplot.xarray
import holoviews as hv
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from cartopy.mpl.geoaxes import GeoAxes
GeoAxes._pcolormesh_patched = Axes.pcolormesh # Helps avoid some weird issues with the polar projection 

# Set page configuration
st.set_page_config(layout="wide")

variables = ("ice_thickness",
             "ice_thickness_int")  # maybe add 'Boxplot' after fixes


with st.beta_container():
    st.title("ICESat-2 data dashboard")
    st.write("""Visualize data on a map projection of the Arctic """)


# User choose type
chosen_var = st.selectbox("Choose your variable", variables)

with st.beta_container():
    st.subheader(f"Showing:  {chosen_va}")
    st.write("")