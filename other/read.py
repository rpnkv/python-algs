import sys

with open('lorem') as lr:
    print(lr.read())

print('-' * 64)

try:
    with open('lorem', newline=',') as lr:
        print(lr.read())
except ValueError:
    print("no way", file=sys.stderr)


