"""Represent a student while preserving the existing CSV field names."""


class Students:
    """Store one student's identity and four subject grades as attributes."""

    # The constructor receives values already validated by the input or CSV layer.
    def __init__(self, full_name, section, spanish, english, social_studies, science):
        """Create a student from values validated by the input or CSV layer."""
        self.full_name = full_name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    @classmethod
    # The from_dict() class method is used to create a Students object from a dictionary, 
    # typically one that has been read from a CSV file. It takes a dictionary (record) as an argument and 
    # unpacks it into the constructor of the Students class using the ** operator. 
    # This allows for easy creation of Students objects from CSV data without needing to manually extract each field.
    def from_dict(cls, record):
        """Build an object from a validated CSV dictionary with numeric grades."""
        return cls(**record) # Unpack the dictionary into the constructor.


    # The to_dict() method is used to convert a Students object back into a dictionary format,
    # which is useful for writing the data back to a CSV file or for other purposes where
    def to_dict(self):
        """Return the original six CSV columns without adding calculated values."""
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science,
        }
