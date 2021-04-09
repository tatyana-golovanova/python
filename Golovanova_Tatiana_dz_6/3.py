import sys
import json


USERS_HOBBIES = {}


with open('users.csv') as user_file:
    with open('hobby.csv') as user_hobbies:
        users = user_file.readlines()
        hobbies = user_hobbies.readlines()

        if len(users) < len(hobbies):
            sys.exit(1)

        for i, item in enumerate(users):
            if i < len(hobbies):
                value = hobbies[i].strip()
            else:
                value = None

            USERS_HOBBIES[item.strip()] = value
        print(USERS_HOBBIES)


with open('users_hobbies.txt', 'w') as output:
    output.write(json.dumps(USERS_HOBBIES))
