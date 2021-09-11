import math

print(" X     sinX      cosX      tanX")
print("=================================")

for i in range(0, 91):
    sinx = math.sin(math.pi * (i / 180))
    cosx = math.cos(math.pi * (i / 180))
    tanx = math.tan(math.pi * (i / 180))

    print("{0:3d}   {1:0.4f}    {2:0.4f}    {3:0.4f}".format(i, sinx, cosx,
                                                             tanx))

print("=================================")