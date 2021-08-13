#!/bin/bash

METHOD=Sieve-hard-to-code
OUTPUT=primenums-stdout.txt

doit() {
  date "+%H:%M:%S $1"
  ./primenums-$METHOD.py $1 >> $OUTPUT
}

echo METHOD: $METHOD > $OUTPUT

doit 10
doit 100
doit 1000
doit 5000
doit 10000
doit 20000
doit 30000
doit 40000
doit 50000
doit 60000
doit 70000
doit 80000
doit 90000
doit 100000
doit 200000
doit 300000
doit 400000
doit 500000
doit 600000
doit 700000
doit 800000
doit 900000
doit 1000000
doit 10000000
doit 100000000
doit 1000000000
