import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    try:
        username = sys.argv[1]
    except IndexError:
        print("Please enter a user ID to query")
        sys.exit()

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)

    print(events[0]['created_at'])
