import random
import json

first_names = ["Nadja", "Nick", "Lucy", "Howie", "Sandy", "AJ", "Vanessa", "Brian", "Jessica", "Kevin"]
last_names = ["Smith", "Johnson", "Brown", "Miller", "Garcia", "Acors", "Alday"]
d= {}
d["First name"] = random.choice(first_names)
d["Last Name"] = random.choice(last_names)
d["Age"] = random.randint(18,99)

string_respresentation = json.dumps(d)
print(string_respresentation)
 
