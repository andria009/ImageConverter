#!/bin/python

import sys, getopt, os
from PIL import Image


def resize(inp, out, qual):
    input_image = Image.open(inp)
    output_image = input_image.convert('RGB')
    output_image.save(out, quality = int(qual))

def main(argv):
    inputfile = ''
    outputfile = ''
    quality = 95

    try:
        opts, args = getopt.getopt(argv,"hi:q:",["ifile=","quality="])
    except getopt.GetoptError:
        print("convert.py -i <inputfile> -q <quality>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("convert.py -i <inputfile> -q <quality>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            outputfile = inputfile[:-4] + ".jpg"
        elif opt in ("-q", "--quality"):
            quality = arg

    resize(inputfile, outputfile, quality)

    inputfile_size = os.path.getsize(inputfile)
    outputfile_size = os.path.getsize(outputfile)
    print("{inp} is converted to {out} reduced = {red:.2f} %.".format(inp = inputfile, out = outputfile, red = outputfile_size * 100/ inputfile_size))

if __name__ == "__main__":
    main(sys.argv[1:])