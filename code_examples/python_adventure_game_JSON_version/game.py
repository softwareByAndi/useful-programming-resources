# display opening monologue
# prompt user input
# take user input
# compare input with branch options
# choose which dialogue to display based on results of input comparison
# rinse and repeat

# 1. create a JSON file with all of our dialogue
# 2. we can create a number of different python scripts for each section of the game
# 3. monolith code -- all dialogue and logic is in a single file.

import json
import importlib
import event
from services import speak

print("")

dialogue_file_name = 'game_start'
while True:
  script = open("scripts/" + dialogue_file_name + '.json');
  script = json.load(script);
  for npc in script['dialogue']:
    if npc['name'] == "":
      speak.narrate(npc['dialogue'])
    else:
      print("%s : "%npc['name'])
      speak.monologue(npc['dialogue'])
    
    if 'events' in npc:
      [event.run(npc['events'], index) for index in range(len(npc['events']))]
      
  next_scene = None
  playerDecision = None
  if 'next_scene' in script:
    next_scene = script['next_scene']
  elif 'prompt' in script:
    while next_scene == None:
      playerDecision = speak.prompt(script['prompt']['options'])
      if playerDecision == 'q':
        print("exiting game...")
        exit()
      try:
        playerDecision = int(playerDecision);
        next_scene = script["prompt"]['next_scene'][playerDecision]
      except:
        next_scene = None
        playerDecision = None
        print("invalid input")
      
    if 'events' in script['prompt']:
      event.run(script['prompt']['events'], playerDecision)

  dialogue_file_name = next_scene
  
