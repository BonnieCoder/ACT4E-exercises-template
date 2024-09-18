from typing import Any, overload, TypeVar
from .my_power_sets import MyFiniteSetOfFiniteSubsets

import act4e_interfaces as I

X = TypeVar("X")


class SolFiniteMakePowerSet(I.FiniteMakePowerSet):
    def powerset(self, s: I.FiniteSet[X]) -> I.FiniteSetOfFiniteSubsets[X, Any]:
        raise NotImplementedError() # implement here

