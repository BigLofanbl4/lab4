#!/usr/bin/env python

speed1 = float(input("Speed of first car (km/h): "))
speed2 = float(input("Speed of second car (km/h): "))
distance = float(input("Distance between cars (kms): "))

print(f"Time of meeting: {round(distance / (speed1 + speed2), 2)}h")
