JSON_KEY = "" # your value here
json = [
  {"foo": "bar"},
  {"quu": "qux"}
  ]

jsonValues = []

for j in json:
  if JSON_KEY in j:
    jsonValues.append(j[JSON_KEY])

print(jsonValues)