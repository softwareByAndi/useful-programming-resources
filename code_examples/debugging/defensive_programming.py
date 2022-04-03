def doSomethingWithText(message):
  assert( str(type(message)) == "<class 'str'>" )
  new_message = "executing code!!! : " + message;
  print(new_message)
  return {
    "asdf": "response",
    "message": new_message
  }

def handleListOfMessages(messages):
  assert(str(type(messages)) == "<class 'list'>")
  responses = []
  for message in messages:
    response = doSomethingWithText(message)
    assert(str(type(response)) == "<class 'dict'>")
    assert(str(type(response.get('asdf', None))) == "<class 'str'>")
    assert(str(type(response.get('message', None))) == "<class 'str'>")
    responses.append(response)

  return responses
  # remove any instances of illegal_words from message

messages = ["m1", {"asdf": "invalid code"}]
responses = handleListOfMessages(messages)
assert(str(type(responses)) == "<class 'list'>")
print(responses)
