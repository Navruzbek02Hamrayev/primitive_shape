from math import sqrt
class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        """
        This method finds the length of line.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return sqrt(abs(self.x1-self.x2)**2+abs(self.y1-self.y2)**2)
line=Line(7,3,3,0)
print(line.get_length())