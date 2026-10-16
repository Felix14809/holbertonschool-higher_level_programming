#!/usr/bin/env python3

"""Save and load Python objects to and from a file"""

import json


def serialize_and_save_to_file(data, filename):

    """Serialize data with and write it to a file"""

    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):

    """Read the file and return the object stored in it"""

    with open(filename, "r") as file:
        return json.load(file)
