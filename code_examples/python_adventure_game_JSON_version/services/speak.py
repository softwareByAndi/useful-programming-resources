import time

from gameData.globals import defaultPause

def monologue(lines, pause = defaultPause):
  for line in lines:
    print("  " + line)
    time.sleep(pause)
  print("");

def narrate(lines, pause = defaultPause):
  print("")
  for line in lines:
    print(line)
    time.sleep(pause)
  print("");

def prompt(options):
  print("")
  print("do you:");
  for index, option in enumerate(options):
    print('  (' + str(index) + ") : " + option)
  playerInput =  input("");
  print("")
  return playerInput