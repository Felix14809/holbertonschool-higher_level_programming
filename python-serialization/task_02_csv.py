#!/usr/bin/env python3
"""Convert a CSV file to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read csv_filename and write its rows to data.json"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
    except Exception:
        return False
    with open("data.json", mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)
        return True
