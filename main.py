from os import environ, system
from replit import db
from requests import get
from json import loads
from sys import stderr, exit, stdout
from requests.exceptions import HTTPError

print("Importing database...")
print("Setting database URL...")

db.db_url = "https://pytest.element1010.repl.co"

print("Successfully set DB URL to https://pytest.element1010.repl.co")

print("Looking for test ID...")
with open("data.json") as testData:
  testData = loads(testData.read())
  id = testData["id"]

print(f"Found test ID: {id}")

print("Looking for test user...")
user = environ["REPL_OWNER"]
print(f"Found test user: {user}")

print("Fetching test...")
try:
  test = get(f"https://raw.githubusercontent.com/element10101/PyTest/main/tests/{id}.json")
  test.raise_for_status()
except HTTPError:
  stderr.write(f"Fetching failed with error code {test.status_code}\n")
  stderr.write("Press Ctrl+C to try again.\n")
  exit(1)
test = loads(test.text)
print(f"Successfully fetched test")

print("Starting test")

system("clear")

cur = 1

for q in test:
  ans = input(q + " \033[38;2;0;255;0m")
  stdout.write("\033[0m")

  db[id][user][cur] = ans
  cur += 1

print("Test completed and submitted.")
