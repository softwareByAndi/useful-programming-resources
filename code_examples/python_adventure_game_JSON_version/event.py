import importlib

def run(events, playerDecision):
  if playerDecision < len(events):
    [event, args] = events[playerDecision]
    if event != None:
      path = event.split('.')
      module = path[-1]
      if len(path) == 1:
        event = importlib.import_module(module)
      else:
        path = '.'.join(path[0:-1])
        event = importlib.import_module('.' + module, path)

      event.run(*args)
