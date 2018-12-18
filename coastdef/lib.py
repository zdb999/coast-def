"""A collection of pre-built functions and model components that you can use in your project.

This library includes climate change models, surge height models, wall cost models, 
and other components.We anticipate that it will grow with time and research; as more people use 
CoastDef, we hope that they will contribute to this library. Whenever possilbe, primary data 
sources are cited."""

# Sea level rise

def quadratic_climate_model(t0,s,b):
  """A function generator that creates a quadratic climate trend

  Args:
    t0 (int): The base year defined in the your model.
    s (float): The linear coefficient of your model.
    b (float): The quadratic coefficient of your model.

  Returns:
    function: Returns a Mean Sea level prediction when provided a year.
    """
  
  def out_function(t):

    msl = s*(t-t0) + b*(t-t0)**2

    return msl

noaa_global_low = quadratic_climate_model(1992, 1.7e-3, 0)
"""NOAA CPO-1 (Parris et al., 2012) Low Estimate"""

noaa_global_intermed_low = quadratic_climate_model(1992, 1.7e-3, 2.71e-5)
"""NOAA CPO-1 (Parris et al., 2012) Intermediate Low Estimate"""

noaa_global_intermed_high = quadratic_climate_model(1992, 1.7e-3, 8.71e-5)
"""NOAA CPO-1 (Parris et al., 2012) Intermediate High Estimate"""

noaa_global_high = quadratic_climate_model(1992, 1.7e-3, 1.56e-4)
"""NOAA CPO-1 (Parris et al., 2012) High Estimate"""


connecticut_intermed_high = quadratic_climate_model(1992, 2.4e-3, 8.71e-5)
"""NOAA CPO-1 (Parris et al., 2012) Intermediate High Estimate"""