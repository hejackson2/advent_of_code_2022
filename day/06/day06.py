#!/usr/bin/env python

data = 'day/06/input'

def findMarker(data, length):
    with open(data, 'r') as f:
        for line in f.readlines():
            t = line.strip()

            for x in range(len(t[:-(length-1)])):
                    s = t[x:x+length]


                    match = False

                    for y in range(length):
                        r = s
                        # print(f'   s:{s}, r:{r}')
                        r = r.replace(s[y],'')

                        if len(r) == length - 1:
                            match = True
                        else:
                            match = False
                            break

                    if match == True:
                        print(f'marker: start:{x+length}, s:{s}\n\n')
                        break



# part one
findMarker(data, 4)

# part two
findMarker(data, 14)

