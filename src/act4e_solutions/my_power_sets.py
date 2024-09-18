from typing import Generic, TypeVar

import act4e_interfaces as I

C = TypeVar["C"]
E = TypeVar["E"]

class MyFiniteSetOfFiniteSubsets(Generic[C, E], I.SetOfFiniteSubsets[C, E], I.FiniteSet[E], I.ABC):
    pass