import re

states = "Mississippi Alabama Texas Massachusetts Kansas"
statesList = []

# Search for a word in variable states that ends in xas
for state in states.split():
    if state.endswith("xas"):
        statesList.append(state)

# Store the word in element 0 of a list named statesList
if statesList:
    statesList[0] = statesList[0].capitalize()

# Search for a word in variable states that begins with k and ends in s
pattern = re.compile(r"\bK\w+s\b", re.I)
matches = pattern.findall(states)
if matches:
    statesList.append(matches[0])

# Search for a word in variable states that begins with M and ends in s
pattern2 = re.compile(r"\bM\w+s\b", re.I)
matches2 = pattern2.findall(states)
if matches:
    statesList.append(matches2[0])

# Search for a word in variable states that ends in a
for state in states.split():
    if state.endswith("a"):
        statesList.append(state)

for state in states.split():
    if state.startswith("M"):
        statesList.append(state)
        break

print(statesList)
