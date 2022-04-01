import json

def cube(num) : return num * 3

myVar = "my variable"

def test_cube() :
  test_cases = {
    1: 1,
    2: 8,
    3: 27,
    4: 64,
    5: 125
  }
  failed = []
  for input in test_cases:
    result = cube(input)
    if result != test_cases[input]:
      failed.append({
        "input": input,
        "expected_output": test_cases[input],
        "actual_output": result
      })

  if failed:
    for entry in failed:
      print("\n", json.dumps(entry, indent=2))
    raise Exception('cube_test() failed')

  print("cube_test() completed successfully!!")

test_cube()