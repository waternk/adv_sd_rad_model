
"""
Python model ASD.py
Translated using PySD version 0.7.2
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'deradicalization': 'deradicalization',
    'unexposed citizens on internet': 'unexposed_citizens_on_internet',
    'exposed citizens on internet': 'exposed_citizens_on_internet',
    'INITIAL TIME': 'initial_time',
    '"% with access to internet"': '_with_access_to_internet',
    'exposure rate': 'exposure_rate',
    'persuasion': 'persuasion',
    'total population': 'total_population',
    'exposure': 'exposure',
    'FINAL TIME': 'final_time',
    'radicalized citizens': 'radicalized_citizens',
    'TIME': 'time',
    'TIME STEP': 'time_step',
    'influence of radicalized': 'influence_of_radicalized',
    'deradicalization rate': 'deradicalization_rate',
    'persuasion rate': 'persuasion_rate',
    'Time': 'time',
    'SAVEPER': 'saveper'}


@cache('run')
def deradicalization_rate():
    """
    deradicalization rate
    ---------------------
    (deradicalization_rate)
    Dmnl

    """
    return 0.02


integ_unexposed_citizens_on_internet = functions.Integ(
    lambda: -exposure(), lambda: total_population() * _with_access_to_internet())


@cache('run')
def persuasion_rate():
    """
    persuasion rate
    ---------------
    (persuasion_rate)
    Dmnl

    """
    return 0.05


@cache('step')
def deradicalization():
    """
    deradicalization
    ----------------
    (deradicalization)
    person/Week

    """
    return radicalized_citizens() * deradicalization_rate()


@cache('run')
def total_population():
    """
    total population
    ----------------
    (total_population)
    person

    """
    return 100


@cache('run')
def _with_access_to_internet():
    """
    "% with access to internet"
    ---------------------------
    (_with_access_to_internet)


    """
    return 0.5


@cache('run')
def exposure_rate():
    """
    exposure rate
    -------------
    (exposure_rate)
    Dmnl

    """
    return 0.1


@cache('step')
def persuasion():
    """
    persuasion
    ----------
    (persuasion)
    person/Week

    """
    return exposed_citizens_on_internet() * persuasion_rate() * influence_of_radicalized()


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Week
    The final time for the simulation.
    """
    return 500


@cache('step')
def exposure():
    """
    exposure
    --------
    (exposure)
    person/Week

    """
    return exposure_rate() * unexposed_citizens_on_internet() * influence_of_radicalized()


integ_exposed_citizens_on_internet = functions.Integ(
    lambda: deradicalization() + exposure() - persuasion(), lambda: 0)


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Week
    The initial time for the simulation.
    """
    return 0


@cache('step')
def unexposed_citizens_on_internet():
    """
    unexposed citizens on internet
    ------------------------------
    (unexposed_citizens_on_internet)
    person

    """
    return integ_unexposed_citizens_on_internet()


@cache('step')
def influence_of_radicalized():
    """
    influence of radicalized
    ------------------------
    (influence_of_radicalized)


    """
    return 0.001 * radicalized_citizens()


@cache('step')
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


integ_radicalized_citizens = functions.Integ(lambda: persuasion() - deradicalization(), lambda: 5)


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Week [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Week [0,?]
    The time step for the simulation.
    """
    return 0.0625


@cache('step')
def radicalized_citizens():
    """
    radicalized citizens
    --------------------
    (radicalized_citizens)
    person

    """
    return integ_radicalized_citizens()


@cache('step')
def exposed_citizens_on_internet():
    """
    exposed citizens on internet
    ----------------------------
    (exposed_citizens_on_internet)
    person

    """
    return integ_exposed_citizens_on_internet()


def time():
    return _t
functions.time = time
functions._stage = lambda: _stage
