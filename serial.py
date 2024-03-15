"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Takes in a start number"""
        self.start = start
        self.next = start
    
    def __repr__(self):
        """Object representation"""
        return f"<SerialGenerator start = {self.start} next = {self.next} >"

    def generate(self):
        """Returns next sequential number"""
        self.next += 1
        return self.next - 1
        
    def reset(self):
        """Resets number back to original start"""
        self.next = self.start



