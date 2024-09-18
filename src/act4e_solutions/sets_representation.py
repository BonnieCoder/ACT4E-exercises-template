from typing import Any
from .my_finite_set_representation import MyFiniteSetRepresentation

import act4e_interfaces as I


class SolFiniteSetRepresentation(I.FiniteSetRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteSet_desc) -> I.FiniteSet[Any]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, f: I.FiniteSet[Any]) -> I.FiniteSet_desc:
        raise NotImplementedError()
