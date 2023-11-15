"""Project Class"""


class Project:
    """Project Class"""
    def __init__(self, name="", start_date=0, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage}")

