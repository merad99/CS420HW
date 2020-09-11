# program that parses an XML file containing an automaton element and extract its states.

import xml.etree.ElementTree as ET
import sys
inp = input()

tree = ET.parse(inp)

root = tree.getroot()

for state in root.iter('state'):
    print(state.get('name'), end=' ')
print()
for state in root.iter('state'):
    for ChildState in state.iter():
        if ChildState.tag == 'initial':
            print(state.get('name'), end=' ')
        elif ChildState.tag == 'final':
            print()
            print(state.get('name'), end=' ')
