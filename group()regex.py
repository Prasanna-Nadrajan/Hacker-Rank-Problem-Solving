import re

s = input()

match = re.search(r'([a-zA-Z0-9])\1', s)

if match:
    print(match.group(1))
else:
    print(-1)
