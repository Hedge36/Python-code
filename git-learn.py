#!/usr/bin/python
import sys
import os
from git import Repo, InvalidGitRepositoryError

def usage(prog_name):
    print("Usage: " + prog_name + " [option]")
    sys.exit(0)

def fatal(message):
    print("fatal: " + message)
    sys.exit(1)

if __name__ == "__main__":
    cur_path = os.getcwd()


    try:
        repo = Repo(cur_path)
    except InvalidGitRepositoryError:
        fatal("not a git repository (or any of the parent directories)")

    # if (len(sys.argv) != 2):
    #    usage("git-learn")

    commits = list(repo.iter_commits('master'))
    print(commits[0])

    if sys.argv[1] == "first" and len(sys.argv) == 2:
        #repo.index.reset(commit=commits[-1])
        os.system("git checkout " + str(commits[-1]))

    if sys.argv[1] == "last" and len(sys.argv) == 2:
        #repo.index.reset(commit=commits[0])
        #os.system("git clean -fdx")
        os.system("git checkout " + str(commits[0]))

    if sys.argv[1] == "next" and len(sys.argv) == 2:
        headcommit = repo.head.commit
        index = commits.index(headcommit)
        if index == 0:
            fatal("not a newer commit (It is the newest commit)")
        os.system("git checkout " + str(commits[index - 1]))

    if sys.argv[1] == "prev" and len(sys.argv) == 2:
        headcommit = repo.head.commit
        index = commits.index(headcommit)
        if index == len(commits) - 1:
            fatal("not a older commit (It is the first commit)")
        os.system("git checkout " + str(commits[index + 1]))
