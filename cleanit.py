#!/usr/bin/python
import sys, getopt
from lib.beautiful_soup import BeautifulSoup

class Cleanit():

    def main(self, argv):
        arguments = self.parseArguments(argv)
        try:
            with open(arguments['input_file'], mode="r") as f:
                soup = BeautifulSoup(f, indentWidth='    ')
        except IOError:
            self.cleanExit("Error: Could not open the input file!")

        try:
            output = open(arguments['output_file'].encode('utf-8','ignore'), "w")
            output.write(soup.prettify())
            output.close()
        except IOError:
            self.cleanExit("Error: Could not write to the output file!")

        sys.exit(0)

        
    def cleanExit(self, msg=""):
        print msg
        print 'cleanit.py -i <inputfile> [-o <outputfile>]'
        sys.exit(1)

    def parseArguments(self, argv):
        input_file = False
        output_file = False

        try:
            opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            self.cleanExit()

        for opt, arg in opts:
            if opt in ("-i", "--ifile"):
                input_file = arg
            if opt == '-h':
                self.cleanExit()
            if opt in ("-o", "--ofile"):
                output_file = arg

        if not input_file:
            self.cleanExit()

        if not output_file:
            output_file = "%s.clean" % (input_file)

        return {
            "input_file": input_file,
            "output_file": output_file,
        }

if __name__ == "__main__":
    Cleanit().main(sys.argv[1:])
