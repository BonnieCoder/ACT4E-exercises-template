from typing import TypeVar
import act4e_interfaces as I
from .my_finite_sets import E

class FiniteSetProperties(I.ABC):

    def is_subset(self, a: I.FiniteSet[E], b: I.FiniteSet[E]) -> bool:
        for i in a.elements():
            k = False
            if b.contains(i):
                k = True

            if k == False:
                return False
        return True
    
    def equal(self, a: I.FiniteSet[E], b: I.FiniteSet[E]) -> bool:
        return self.is_subset(a, b) and self.is_subset(b, a)
    
    def is_strict_subset(self, a: I.FiniteSet[E], b: I.FiniteSet[E]) -> bool: 
        return self.is_subset(a, b) and not self.is_subset(b, a)