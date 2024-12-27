#!/usr/bin/python
import glob
import multiprocessing
import os
import sys

import binaryninja


def analyze_file(file_path):
    print(f"Analyzing file {file_path}.")

    # analyze with binaryninja
    with binaryninja.load(file_path) as bv:
        bv.update_analysis_and_wait()

        # save analysis database in filesystem
        bv.create_database(f"{file_path}.bndb")

    return file_path


if __name__ == "__main__":
    # check file arguments
    if len(sys.argv) < 2:
        print("[*] Syntax: {} <path to analysis directory>".format(sys.argv[0]))
        exit(0)

    # parse arguments
    analysis_directory = sys.argv[1]

    # analyze files in parallel
    with multiprocessing.Pool() as pool:
        mapping = pool.map(
            analyze_file,
            [
                file_path
                for file_path in glob.glob(f"{analysis_directory}/*")
                if not file_path.endswith(".bndb")
                and not os.path.exists(file_path + ".bndb")
            ],
        )
