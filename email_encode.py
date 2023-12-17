#!/usr/bin/env python

import sys

if __name__ == "__main__":
    email = sys.argv[1]
    encoded = ''.join(['&#%d;' % ord(x) for x in email])
    print(encoded)