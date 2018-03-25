#!/usr/bin/env python
import os
import sys
import json
from trips.models import Course

courseid_file = '../courseid.json'
courses_file = '../data/courses_with_courseid.json'
sims_file = '../data/course_batch_final_with_title.json'

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytestsite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Read the course data
    with open(courses_file, 'r') as f:
        with open(sims_file, 'r') as f2:
            with open(courseid_file, 'r') as f3:
                datas = json.loads(f.readlines()[0])
                sims = json.loads(f2.readlines()[0])
                nyu_course_ids = json.loads(f3.readlines()[0])
                err_cnt = 0
                crt = 0
                for d in datas:
                    try:
                        sim = sims[d['course_title']]
                    except KeyError:
                        # print(d['course_title'])
                        sim = {}

                    try:
                        instructor = d['instructor_name']
                    except KeyError:
                        instructor = "N/A"

                    try:
                        nyu_course_id = d['nyu_course_id'].replace(' ', '').replace('-', '')
                    except KeyError:
                        nyu_course_id = "N/A"

                    try:
                        tid = nyu_course_ids[nyu_course_id]['tid']
                        score = nyu_course_ids[nyu_course_id]['score']
                        crt += 1
                        print(crt, d['course_title'], nyu_course_id)

                    except KeyError:
                        err_cnt += 1
                        # print(err_cnt, nyu_course_id)
                        tid = 0
                        score = "N/A"

                    Course.data[d['course_title']] = Course(d['course_id'], nyu_course_id, 
                                                            d['course_title'], d['course_descr'],
                                                            score, d['class_type_descr'],
                                                            instructor, tid, sim)

    execute_from_command_line(sys.argv)
