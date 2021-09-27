# Room class example

class Room:
    """
    Holds data for individual rooms in the adventure.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        """Returns a human readable version of the object"""
        return("Location: " + self.name + " \nDescription: " + self.description)
        
"""
NOTE:
    it's defined as __init__
    but it's called as Room()
"""

