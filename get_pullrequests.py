import re
import os
import json
import requests


def get_last_processed():
    last_processed = 0
    if os.path.exists("last_processed.txt"):
        with open("last_processed.txt") as file:
            last_processed = int(file.read())
    return last_processed

def save_processed(last_processed):
    with open("last_processed.txt", "w") as file:
        file.write(str(last_processed))

def get_repositories(last_processed=0):
    new_repositories = {}
    just_processed = last_processed

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    page = 0
    per_page = 100
    continue_process = True
    while continue_process:
        page += 1
        pull_requests = requests.get(
            f"https://api.github.com/repos/hacs/default/pulls?state=open&&per_page={per_page}&page={page}",
            headers=headers).json()
        if len(pull_requests) == 0:
            continue_process = False
        for pull_request in pull_requests:
            if "number" not in pull_request:
                print("Rate limit reached...")
                continue_process = False
                break
            if pull_request["number"] <= last_processed:
                continue_process = False
                break
            match = re.search(r"Adds new (.*) \[(.*)\]", pull_request["title"])
            if match:
                new_repositories.setdefault(match[1], []).append(match[2])
                if pull_request["number"] > just_processed:
                    just_processed = pull_request["number"]
            else:
                # print(pull_request["title"])
                continue

    return new_repositories, just_processed


def append_repositories(new_repositories):
    for rep_item, repositories in new_repositories.items():
        prev_repositories = []
        if os.path.exists(rep_item):
            with open(rep_item) as file:
                prev_repositories = json.load(file)
        content = list(set(prev_repositories + repositories))
        with open(rep_item, "w") as file:
            file.write(json.dumps(sorted(content, key=str.casefold), indent=2))



last_processed = get_last_processed()
new_repositories, just_processed = get_repositories(last_processed)
print(new_repositories)
append_repositories(new_repositories)
save_processed(just_processed)
