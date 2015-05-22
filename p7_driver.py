import subprocess
import json
import collections
import random
import sys
import shlex

def solve(args):
    """Run clingo with the provided argument list and return the parsed JSON result."""
    
    GRINGO = "gringo level-core.lp level-style.lp level-sim.lp level-shortcuts.lp ^ | reify ^ | clingo - meta.lp metaD.lp metaO.lp metaS.lp ^ --parallel-mode=4 --outf=2 > "+ args
    #word = []
    #word.append(args)
    #G = []
    #G = shlex.split(GRINGO)
    #D = []
   # D.append(">")
    print args


    clingo = subprocess.check_output(GRINGO, shell=True)
    #out, err = clingo.communicate()
    #if err:
      #  print err
        
    return
    
def main(argv):
    #prog, filename = argv
   # args = []
    filename = raw_input("What would you like to call this map?")
    filename += ".json"
    solve(filename)

    #with open(filename) as file:
    #    fileDict = parse_json_result(file)

if __name__ == '__main__':
  main(sys.argv)