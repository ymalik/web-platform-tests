#!/usr/bin/env python

import json
import subprocess
import os

def call(**args):
    return subprocess.check_call(args)


def get_manifest(rev):
    call("git", "checkout", rev)
    call("./manifest")
    with open("MANIFEST.json") as fp:
        #return json.load(fp)
        return fp.readlines()


def main():
    head = os.environ['TRAVIS_COMMIT']
    merge_base = call("git", "merge-base", "master", head).strip()
    before = get_manifest(merge_base)
    after = get_manifest(head)
    for line in unified_diff(before, after, fromfile='before.json', tofile='after.json'):
        print(line)


if __name__ == "__main__":
    main()
