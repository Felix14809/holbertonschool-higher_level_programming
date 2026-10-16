#!/usr/bin/env python3
"""Defines CustomObject, that can save itself to and load itself from a file"""
import pickle


class CustomObject:
    """A person with a name, an age, and a student status."""

    def __init__(self, name="", age=0, is_student=False):
        """Initialize with a name, an age and if the person is a student"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize this object with pickle and save it to filename."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Load and return the object stored in filename, or None"""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj if isinstance(obj, cls) else None
        except Exception:
            return None

    def display(self):
        """Print the name, age and student status of this object."""
        print(f"Name: {self.name}\nAge: {self.age}\n"
              f"Is Student: {self.is_student}")
