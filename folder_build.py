#!/bin/python3

import os
import shutil
import sys


def get_students(text_file):
    students = {}
    name = 'ERROR'
    with open(text_file) as raw_list:
        for line in raw_list:
            if ',' in line and '@' not in line:
                name = " ".join([n.strip() for n in reversed(line.split(','))])
            if '@' in line:
                students[name] = line.strip()
    return students


def populate(students, template, main_path):
    for student in students:
        shutil.copytree(template, os.path.join(main_path, student.replace(" ", "_")))


def build_drive(text_file, template, main_path):
    students = get_students(text_file)
    populate(students, template, main_path)
    

def main(args):
    if len(args) < 4:
        print("folder_build.py student_list_file student_templat_folder class_root")
        return
    
    build_drive(args[1], args[2], args[3])

if __name__ == "__main__":
    main(sys.argv)

        
        
                
                
