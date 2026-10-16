#!/usr/bin/env python3
"""Serializes dicts to XML files and deserializes xml files """
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Save a dict to filename as XML."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Load the XML in filename and return it as a dict."""
    tree = ET.parse(filename)
    root = tree.getroot()
    xml_dict = {}
    for child in root:
        xml_dict[child.tag] = child.text
    return xml_dict
