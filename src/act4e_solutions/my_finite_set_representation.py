from typing import TypeVar 
from .my_finite_sets import MyFiniteSet
import act4e_interfaces as I 

E = TypeVar("E")

class MyFiniteSetRepresentation(I.FiniteSetRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteSet_desc) -> I.FiniteSet[E]:
        if not isinstance(data, dict):
            raise I.InvalidFormat()
        # note: later on the format will be extended
        if not "elements" in data:
            raise I.InvalidFormat()
        if not isinstance(data["elements"], list):
            raise I.InvalidFormat()
        elements = data["elements"]
        return MyFiniteSet(elements)
    def save(self, h: I.IOHelper, f: I.FiniteSet[E]) -> I.FiniteSet_desc:
        all_elements = [f.save(h, _) for _ in f.elements()]
        return {"elements": all_elements}