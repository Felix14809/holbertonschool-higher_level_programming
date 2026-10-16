#!/usr/bin/env python3
"""Save and load Python objects to and from a file using pickle."""
import pickle


def serialize_and_save_to_file(data, filename):
    """Serialize data with pickle and write it to filename."""
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """Read filename and return the object stored in it."""
    with open(filename, "rb") as file:
        return pickle.load(file)
