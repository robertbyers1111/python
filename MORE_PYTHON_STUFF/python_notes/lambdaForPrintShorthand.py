#!/usr/bin/python3

# Lambda to customize a print function.

import sys
lprint=lambda *args:sys.stdout.write(" ".join(map(str,args)))
lprint("python", "tips",1000,1001)

#-> python tips 1000 1001
