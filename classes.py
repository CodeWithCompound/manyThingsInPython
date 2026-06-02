from dataclasses import dataclass, field, asdict, replace
from typing import List
from decimal import Decimal
# what i learned:
# kw_only (line 6) enforces you to include the arguments (see line XXXXXXXX)
# not code related but sku means stock keeping unit 
# rounding (line xxxxxxxxxxxx) to the second decimal point
# @property (line xxxxxxxxxxxx) lets you write x.atr instead of x.atr()
# repr=False (line xxxxxxxxxxx) makes the whole field not appear and is,  from what i gathered great for internal use 
# field(default_factory=list) (line xxxxxxxxx) prevents a bug where, if it was "tags: list =[]" it would make every product point to this ONE list, which we don't want
@dataclass(frozen=True, slots=True, kw_only=True)
class Product:
    sku: str 
    name: str
    price: Decimal
    tags: List[str] = field(default_factory=list) 
    in_stock: bool = True
    _discount: Decimal = field(default=Decimal("0"), init=False, repr=False)

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price can't be negative")
        if "sale" in self.tags:
            object.__setattr__(self, "_discount", self.price * Decimal("0.1")) 
        
    @property
    def final_price(self) -> Decimal:
        return self.price - self._discount 

    def apply_discount(self, percent: Decimal) -> "Product":
        new_price = self.price * (1 - percent / 100)
        return replace(self, price=new_price)


p = Product(sku="LAPTOP-001", name="MacBook Pro", price=Decimal("1999.99"), tags=["electronics"])
print(p.final_price)

p2 = p.apply_discount(Decimal("5"))
print(f"After 5% discount:", round(p2.final_price, 2))