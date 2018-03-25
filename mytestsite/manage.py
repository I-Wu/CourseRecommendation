#!/usr/bin/env python
import os
import sys
import json
from trips.models import Course

courses_file = '../data/src/courses_with_instructor.json'
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
            datas = json.loads(f.readlines()[0])
            sims = json.loads(f2.readlines()[0])
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

                Course.data[d['course_title']] = Course(d['course_id'], d['course_title'],
                                                        d['course_descr'], 0, d['class_type_descr'],
                                                        instructor, 577620, sim)

    execute_from_command_line(sys.argv)
