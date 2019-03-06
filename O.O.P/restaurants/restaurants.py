class Restaurant(object):
    """A restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and the cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe(self):
        """Describe the restaurant."""
        print "Name:", self.restaurant_name.title(), "cuisine type:", self.cuisine_type

    def open(self):
        """Simulates the opening of the restaurant."""
        print self.restaurant_name.title(), "is now open."
