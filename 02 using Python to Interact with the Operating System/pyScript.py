#!/usr/bin/env python3

import re
import sys


def listToDictandCSV(errors):
    #  my_list = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5]
    unique_items = set(errors)
    Dict = {item: errors.count(item) for item in unique_items}
    # sort the dict by value
    Dict = dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True))
    with open("error_message.csv", "w") as f:
        f.write("Error,Count\n")
        for key in Dict.keys():
            f.write(key + "," + str(Dict[key]) + "\n")
    return Dict


fileloc = sys.argv[1]
pattern = r"ticky: ERROR:? ([\w ']*) "
errors = []

with open(fileloc) as f:
    file = f.readlines()
    # print(type(file))
    #  print(file)
    for line in file:
        result = re.search(pattern, line.strip())
        ## from result extract the group noly
        if result:
            # print(result.group(1))
            errors.append(result.group(1))
            # print(result)

Dict = listToDictandCSV(errors)
# print(Dict)

# from syslog.log extract the user name
pattern = r"\(([\w ']*)\)"
users = []
userdict = {}
with open(fileloc) as f:
    file = f.readlines()
    # print(type(file))
    #  print(file)
    for line in file:
        result = re.search(pattern, line.strip())
        ## from result extract the group noly
        if result:
            user = result.group(1)
            # print(result.group(1))
            users.append(result.group(1))
            if user not in userdict:
                userdict[user] = {"INFO": 0, "ERROR": 0}
            else:
                if "ERROR" in line:
                    userdict[user]["ERROR"] += 1
                elif "INFO" in line:
                    userdict[user]["INFO"] += 1

# userdict to csv
# sort the dict by key
userdict = dict(sorted(userdict.items(), key=lambda item: item[0]))
with open("user_statistics.csv", "w") as f:
    f.write("Username,INFO,ERROR\n")
    for key in userdict.keys():
        f.write(
            key
            + ","
            + str(userdict[key]["INFO"])
            + ","
            + str(userdict[key]["ERROR"])
            + "\n"
        )
        # print(result)
# print(userdict)
# comment all print statements
