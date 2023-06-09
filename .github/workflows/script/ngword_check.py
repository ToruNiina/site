import glob
import os
import sys

NGWORD_LIST = [
    ("", "<br>", "<br/>"),
    ("", "</br>", "<br/>"),
    ("", "algined", "aligned"),
    ("", "condtion", "condition"),
    ("", "eror", "error"),
    ("", "exposion", "exposition"),
    ("", "noexpcet", "noexcept"),
    ("", "protmise_type", "promise_type"),
    ("", "repear", "repeat"),
    ("", "子ルーチン", "コルーチン"),
    ("", "移譲", "委譲"),
    ("reference/chrono", "dulation", "duration"),
    ("reference/random", "施行", "試行"),
    ("reference/random", "疑似", "擬似"),
]

def check_ngword(text: str, filename: str) -> bool:
    found_error: bool = False

    for target_dir, ngword, correct in NGWORD_LIST:
        if not filename.startswith(target_dir):
            continue

        if ngword in text:
            print("{}: the file includes ngword \"{}\". you should fix to \"{}\".".format(filename, ngword, correct))
            found_error = True
    return not found_error

if __name__ == '__main__':
    found_error = False
    current_dir = os.getcwd()
    outer_link_dict = dict()
    found_error = False
    for p in sorted(list(glob.glob("**/*.md", recursive=True))):
        with open(p) as f:
            text = f.read()

        if not check_ngword(text, p):
            found_error = True

    if found_error:
        sys.exit(1)