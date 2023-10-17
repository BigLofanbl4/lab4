#!/usr/bin/env python
import math

y = float(input("Enter angle: "))
hours = math.floor(y * 2 / 60)
minutes = math.floor(y * 2 - (hours * 60))

print(f"{hours} hours {minutes} minutes")
