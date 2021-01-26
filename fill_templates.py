import argparse
import os
import glob
import jinja2

def find_diffs(filter_string: str):
    """
    Find a list of files that have changed according to git status. 
    Filter them by regex string. 
    """
    return os.system(f"git diff --name-only | grep {filter_string}")


def create_html(ipynb_files: list[str], folder: str):
    """
    Give it a list of ipynb files and a folder and a folder. 
    Will convert the notebooks to html and save them in the folder. 
    """
    for file in ipynb_files:
        os.system(f"jupyter nbconvert --to_html {file} {folder}")


def fill_template():
    pass

if __name__ == "__main__":
    pass