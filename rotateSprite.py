#!/usr/bin/env python3
# 16 x 16 array rotation
# Based in the answer from StackOverflow: https://stackoverflow.com/questions/35510361/how-to-rotate-a-bidimensional-byte-array/71307644#71307644
# These equations give you the coordinates (x',y') of the element corresponding to the coordinates (x,y):
# 
# x' =  c * x + s * y - a * (1 - c - s)
# y' = -s * x + c * y - a * (1 - c + s)
# where
# 
# c = cos(-theta)
# s = sin(-theta)
# a = +0.5 - 0.5 * N
# N = side length of your square collision map (i.e. 16)
# theta = angle of clockwise rotation
        # (but effectively counter-clockwise for the way that you
        # usually visualize arrays, i.e. y-axis pointing downwards)
        # So f(x,y) is the function returning x' and y'.

from math import sin,cos,floor,ceil
import argparse
import os,time

#Parsing arguments from the command line
argument=argparse.ArgumentParser(description='Rotate sprites from tinysprite ')
argument.add_argument('--input', required=True, help='Backup file from tinysprite')
argument.add_argument('--output',default="tinysprite.spr", help='Destination file')
argument.add_argument('--theta',default=0.1, help='Angle value')
argument.add_argument('--interval', default=0.2, help='Time interval between frames. Defaul=0.2')
argument.add_argument('--frames',default=6.2, help='Number of frames to generate. Default=6.2')

args=argument.parse_args()
#print(args.input)
height = 16
width = 16
angle = 0


# Because python is weird sometimes - https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
tmp= [ [0]*16 for i in range(16)]
bitmap= [ [0]*16 for i in range(16)]

#My bitmap is actually a sprite pattern
x=0
with open(args.input) as file:
    for line in file:
        if (len(line)>=16):
            line=line.replace(".","0")
            for y in range(0,len(line)-1):
                if line[y:y+1] in "ABCDFEF":
                    bitmap[x][y]=str(line[y:y+1])
                if line[y:y+1] in "012345678":
                    bitmap[x][y]=int(line[y:y+1])
            x=x+1
file.close()

# Palete definition:https://paulwratt.github.io/programmers-palettes/HW-MSX/HW-MSX-palettes.html
# ANSI codes: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
def colorMe(hexVal):
    if (hexVal == 0):
            return "\u001b[38;5;00m0\u001b[0m"
    if (hexVal == 1):
            return "\u001b[47m\u001b[38;5;00m1\u001b[0m"
    if (hexVal == 2):
            return "\u001b[38;5;34m2\u001b[0m"
    if (hexVal == 3):
            return "\u001b[38;5;40m3\u001b[0m"
    if (hexVal == 4):
            return "\u001b[38;5;20m4\u001b[0m"
    if (hexVal == 5):
            return "\u001b[38;5;27m5\u001b[0m"
    if (hexVal == 6):
            return "\u001b[38;5;124m6\u001b[0m"
    if (hexVal == 7):
            return "\u001b[38;5;14m7\u001b[0m"
    if (hexVal == 8):
            return "\u001b[38;5;160m8\u001b[0m"
    if (hexVal == 9):
            return "\u001b[38;5;1m9\u001b[0m"
    if (hexVal == "A"):
            return "\u001b[38;5;220mA\u001b[0m"
    if (hexVal == "B"):
            return "\u001b[38;5;222mB\u001b[0m"
    if (hexVal == "C"):
            return "\u001b[38;5;28mC\u001b[0m"
    if (hexVal == "D"):
            return "\u001b[38;5;129mD\u001b[0m"
    if (hexVal == "E"):
            return "\u001b[38;5;244mE\u001b[0m"
    if (hexVal == "F"):
            return "\u001b[38;5;15mF\u001b[0m"

output=open(args.output,'w+')
output.write("!type\r\nmsx1\r\n")

while(angle <= float(args.frames)):
    os.system('clear')
    output.write("#slot %s\r\n"%round(angle,2))
    for x in range (0,height):
        for y in range(0,width):
            rx =  cos(-angle) * x + sin(-angle) * y - (+0.5 - (0.5 * height)) * ( 1 - cos(-angle) - sin(-angle))
            ry = -sin(-angle) * x + cos(-angle) * y - (+0.5 - (0.5 * width))  * ( 1 - cos(-angle) + sin(-angle))
            if ( round(rx) >= 0 and round(rx) < width and round(ry) >= 0 and round(ry) < height):
                tmp[x][y]=bitmap[round(rx)][round(ry)]
            else:
                tmp[x][y]=0
        #print("\r\n",end='')
    
    for x in range (0,height):
        print("\t\t",end='' )
        for y in range(0,width):
            print("%s"% colorMe(tmp[x][y]),end='')
            if (tmp[x][y]) == 0:
                output.write(".")
            else:
                output.write ("%s"%tmp[x][y])
        print("\r\n", end='')
        output.write("\r\n")

    print("\r\nTheta: %s"%round(angle,2))
    angle = angle + float(args.theta)
    time.sleep(float(args.interval))
    
output.close()


