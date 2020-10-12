"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    # Class attribute
    cache = {}
    
    # Instance attributes
    def __init__(self, name, flavor, price):
        """Create a Cupcake."""

        self.name = name
        self.qty = 0
        self.flavor = flavor
        self.price = price
        self.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'
    

    # Instance Methods
    def add_stock(self, amount):
        """Add cupcakes to stock."""

        self.qty += amount


    def sell(self,amount):
        """Sell cupcakes in stock."""

        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
        elif self.qty < amount:
            self.qty = 0 
        else:
            self.qty -= amount

    
    # Static Methods
    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale the ingredients by the given amount of cupcakes."""

        recipe_scaled = []

        for ingredient in ingredients:
            ingredient = (ingredient[0], ingredient[1] * amount)
            recipe_scaled.append(ingredient)
        
        return recipe_scaled

    
    # Class Methods
    @classmethod
    def get(cls, name):
        """Return a cupcake from cache."""

        if name in cls.cache:
            return cls.cache[name]
        else:
            print("Sorry, that cupcake doesn't exist")


# Further Study
class Brownie(Cupcake):
    """A Brownie."""

    def __init__(self, name, price):
        """Create a Brownie."""

        super().__init__(name, "chocolate", price)


# Doctest results
if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
