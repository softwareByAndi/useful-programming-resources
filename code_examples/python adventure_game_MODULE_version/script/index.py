from . import _choose_bravery
from services import speak
from gameData.player import obtainItem;
from .outside import go_to_village

def script():
  print("")
  speak.monologue([
    "hello world",
    "my name is..",
    "it's, umm..",
    "hmm. It appears I've forgotten my name...",
    "...",
    "oh! Right! it's Greg!",
    "my name is Greg!",
    "fear me, for I am Greg!"
  ])

  playerDecision = input("do you fear Greg? (y/n)");
  
  if playerDecision == "y" or playerDecision == "Y":
    option_search = 1;
    option_run = 2;
    speak.monologue([
      "you are very afraid!",
      "as you avert your eyes, you see something out glint from under a pile of dirt"
    ])

    playerDecision = speak.prompt([
      "(%s) : look under the dirt"%option_search,
      "(%s) : run away"%option_run
    ])
    if playerDecision == str(option_search):
      speak.monologue([
        "you take a risk and search the dirt.",
        "...",
        "Greg is confused, and appears to be annoyed that you are ignoring him",
        "but you pay it no mind.",
        "",
        "in the dirt you find something interesting...",
        "this may turn the tide of battle!",
        "",
        ""
      ])
      obtainItem("sword")

      option_fight = 1;
      playerDecision = speak.prompt([
        "(%s) : fight"%option_fight,
        "(%s) : run"%option_run
      ])
      if playerDecision == str(option_fight):
        speak.monologue([
          "with your rusty sword, you kill Greg ...",
          "turns out he was actually pretty weak...",
          "there was probably nothing to be afraid of",
          "",
          "covered in blood, you exit the cave",
        ])

    if playerDecision == str(option_run):
      speak.monologue([
        "you successfully run away!",
        "covered in sweat, snot and tears, you exit the cave"
      ])

    go_to_village.script()

  else:
    _choose_bravery.main()