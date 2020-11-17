#!/usr/bin/env python3
import random
f = open("/var/www/html/result.dat", "w")
for i in range (20):
    f.write("%d\t%d\t%d\t%d\t\n" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
f.close()
