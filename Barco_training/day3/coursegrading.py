# TODO: finish this
import argparse
import os
import zipfile


def check_name(zip_file):
    (head, tail) = os.path.split(zip_file)
    split_tail = tail.split("-")
    result = False
    if len(split_tail) == 3:
        result = True
    else:
        result = False

    return result


def unpack_all(zip_file):
    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(os.curdir)


def check_directories():
    exercises_tuple = os.walk("Exercises").next()
    exercises = exercises_tuple[1]

    expected_exercises = ['classes', 'data_types', 'exceptions', 'functions', 'modules',
                          'strings', 'iterators', 'user_iterators', 'filesystem']
    found_exercises = []
    lacking_exercises = []
    for exercise in exercises:
        if exercise in expected_exercises:
            found_exercises.append(exercise)
        else:
            lacking_exercises.append(exercise)

    print "Found exercise directories"
    for d in found_exercises:
        print "     " + d
    print
    print "Lacking exercise directories"
    for d in lacking_exercises:
        print "     " + d


def check_files():
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--zip-file", dest="zip_file", type=str, required=True,
                        help="The name of the ZIP-file to check.")
    args = parser.parse_args()

    unpack_all(args.zip_file)
    check_directories()
