# Name: XML 1 - Find the Score
# Problem: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
# Score: 20


import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    atts = len(node.attrib)
    for child in node:
        atts += get_attr_number(child)
    return atts 


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
