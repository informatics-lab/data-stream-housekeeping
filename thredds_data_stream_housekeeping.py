"""


"""

import os, time, sys

MAX_FILE_AGE = 24 * 60 * 60 # In seconds
SLEEP_TIME = 15 * 60 # In seconds
PATH = os.getenv('DATA_DIR')
NOW = time.time()

def main():
    for f in os.listdir(PATH):
        f = os.path.join(PATH, f)
        if os.stat(f).st_mtime < NOW - MAX_FILE_AGE:
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))

    time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
