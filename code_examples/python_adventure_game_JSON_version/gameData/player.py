from services.speak import narrate;

inventory = []
name = "greg"
health = 100
gold = 0


def obtainItem(item):
  narrate(["you've obtained a %s!"%item]);
  global inventory
  inventory.append(item);
  print('  inventory: ', inventory)
  print("\n")