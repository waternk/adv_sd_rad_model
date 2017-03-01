
"""
Python model ASD_V2.py
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
    'number of foreign fighters': 'number_of_foreign_fighters', 'exposure': 'exposure',
    'deradicalization': 'deradicalization', 'persuasion rate': 'persuasion_rate',
    'TIME STEP': 'time_step', 'Time': 'time', 'FINAL TIME': 'final_time',
    'deradicalization rate': 'deradicalization_rate', 'total population': 'total_population',
    'percent of muslims in population': 'percent_of_muslims_in_population',
    'unexposed citizens on internet': 'unexposed_citizens_on_internet',
    'radicalized citizens': 'radicalized_citizens',
    'exposed citizens on internet': 'exposed_citizens_on_internet', 'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper', 'exposure rate': 'exposure_rate', 'persuasion': 'persuasion',
    'percent with access to internet': 'percent_with_access_to_internet', 'TIME': 'time'}


@cache('step')
def unexposed_citizens_on_internet():
    """
    unexposed citizens on internet
    ------------------------------
    (unexposed_citizens_on_internet)
    person [0,?]

    """
    return integ_unexposed_citizens_on_internet()


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


@cache('step')
def exposure():
    """
    exposure
    --------
    (exposure)
    person/Week

    """
    return exposure_rate() * unexposed_citizens_on_internet()


integ_radicalized_citizens = functions.Integ(
    lambda: persuasion() - deradicalization(),
    lambda: 0.005 * total_population())


@cache('run')
def exposure_rate():
    """
    exposure rate
    -------------
    (exposure_rate)
    Dmnl

    """
    return 0.1


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


delay_radicalized_citizensderadicalization_rate_12_0_1 = functions.Delay(
    lambda: radicalized_citizens() * deradicalization_rate(), lambda: 12, lambda: 0, lambda: 1)


@cache('step')
def exposed_citizens_on_internet():
    """
    exposed citizens on internet
    ----------------------------
    (exposed_citizens_on_internet)
    person

    """
    return integ_exposed_citizens_on_internet()


@cache('run')
def percent_with_access_to_internet():
    """
    percent with access to internet
    -------------------------------
    (percent_with_access_to_internet)


    """
    return 0.5


@cache('run')
def deradicalization_rate():
    """
    deradicalization rate
    ---------------------
    (deradicalization_rate)
    Dmnl

    """
    return 0.02


@cache('step')
def persuasion():
    """
    persuasion
    ----------
    (persuasion)
    person/Week

    """
    return delay_exposurepersuasion_rate_4_0_1()


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Week
    The final time for the simulation.
    """
    return 100


integ_unexposed_citizens_on_internet = functions.Integ(
    lambda: -exposure(), lambda: total_population() * percent_with_access_to_internet())


@cache('step')
def deradicalization():
    """
    deradicalization
    ----------------
    (deradicalization)
    person/Week

    """
    return delay_radicalized_citizensderadicalization_rate_12_0_1()


integ_exposed_citizens_on_internet = functions.Integ(
    lambda: deradicalization() + exposure() - persuasion(), lambda: 0)


@cache('run')
def number_of_foreign_fighters():
    """
    number of foreign fighters
    --------------------------
    (number_of_foreign_fighters)
    person

    """
    return 100


@cache('step')
def persuasion_rate():
    """
    persuasion rate
    ---------------
    (persuasion_rate)
    Dmnl

    """
    return number_of_foreign_fighters() / (percent_of_muslims_in_population() * total_population())


@cache('step')
def radicalized_citizens():
    """
    radicalized citizens
    --------------------
    (radicalized_citizens)
    person

    """
    return integ_radicalized_citizens()


@cache('run')
def percent_of_muslims_in_population():
    """
    percent of muslims in population
    --------------------------------
    (percent_of_muslims_in_population)


    """
    return 0.5


@cache('run')
def total_population():
    """
    total population
    ----------------
    (total_population)
    person

    """
    return 1.31105e+09


delay_exposurepersuasion_rate_4_0_1 = functions.Delay(
    lambda: exposure() * persuasion_rate(),
    lambda: 4, lambda: 0, lambda: 1)


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
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


def time():
    return _t
functions.time = time
functions._stage = lambda: _stage
