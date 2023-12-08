#!/usr/bin/env python3

import re
import sys
import csv

fileloc = sys.argv[1]
error_message = {}
user_statistics = {}


def error_message_csv(error_message):
    with open("error_message.csv", "w") as f:
        # write csv by DictWriter object
        csvw = csv.DictWriter(f, fieldnames=["Error", "Count"])
        csvw.writeheader()
        for key in error_message.keys():
            csvw.writerow({"Error": key, "Count": error_message[key]})


def user_statistics_csv(user_statistics):
    with open("user_statistics.csv", "w") as f:
        # write csv by DictWriter object
        csvw = csv.DictWriter(f, fieldnames=["Username", "INFO", "ERROR"])
        csvw.writeheader()
        for key in user_statistics.keys():
            csvw.writerow(
                {
                    "Username": key,
                    "INFO": user_statistics[key]["INFO"],
                    "ERROR": user_statistics[key]["ERROR"],
                }
            )


def generate_report(fileloc):
    with open(fileloc) as f:
        lines = f.readlines()
        for line in lines:
            user = re.search(r"\(([\w. ]*)\)", line.strip()).group(1)
            print(user)
            if "ERROR" in line and user:
                error = re.search(r"ERROR ([\w ]*) ", line.strip()).group(1)
                print(error)
                if error not in error_message:
                    error_message[error] = 1
                else:
                    error_message[error] += 1
                if user not in user_statistics:
                    user_statistics[user] = {"INFO": 0, "ERROR": 0}
                else:
                    user_statistics[user]["ERROR"] += 1
            if "INFO" in line:
                if user not in user_statistics:
                    user_statistics[user] = {"INFO": 0, "ERROR": 0}
                else:
                    user_statistics[user]["INFO"] += 1


if __name__ == "__main__":
    generate_report(fileloc)
    error_message_csv(error_message)
    user_statistics_csv(user_statistics)
    print(len(error_message.keys()))
    print(len(user_statistics.keys()))