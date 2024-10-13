class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Calculate the area of the shape.

        Raises:
            NotImplementedError: If this method is not overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize a rectangle with given length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        import math  # Import math module for pi
        return math.pi * self.radius ** 2