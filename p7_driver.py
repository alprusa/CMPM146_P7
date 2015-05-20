import subprocess
import json
import collections
import random
import sys

def solve(*args):
    """Run clingo with the provided argument list and return the parsed JSON result."""
    
    CLINGO = "./clingo-4.5.0-win64/clingo-4.5.0-win64/clingo"
    
    clingo = subprocess.Popen(
        [CLINGO, "--outf=2"] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = clingo.communicate()
    if err:
        print err
        
    return parse_json_result(out)
    
def main(argv):
    prog, filename = argv
        
    #with open(filename) as file:
    #    fileDict = parse_json_result(file)

if __name__ == '__main__':
  main(sys.argv)