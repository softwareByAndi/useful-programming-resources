from gameData.player import gold
from services.speak import narrate

def run(amount):
  narrate(["you've obtained " + str(amount) + " gold!"])
  global gold
  gold += amount
  print("gold: ", gold)