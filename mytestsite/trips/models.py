from django.db import models
import re

class Course():
    """The model for a course."""

    data = {}

    def __init__(self, cid, nyu_course_id, title, description, rating, class_type, 
                 instructor, tid, recommendation):
        """ Initialize a Course recommendation """
        self.id = cid
        self.nyu_course_id = nyu_course_id
        self.title = title
        self.description = description
        self.rating = rating
        self.class_type = class_type
        self.instructor = instructor
        self.tid = tid
        self.recommendation = recommendation

    @staticmethod
    def get_match(keyword):
        return [k for k, v in Course.data.items() if re.search(keyword, k, re.IGNORECASE)]

    @staticmethod
    def get_course(course_name):
        return Course.data[course_name]

    @staticmethod
    def get_recommend_courses(course_name):
        """Get a dictionary of the course and their descriptions."""
        recs = Course.get_recommend(course_name)
        ret = []
        for rec in recs:
            ret.append([Course.data[cname] for cname, _ in rec.items()])
        return ret

    @staticmethod
    def get_recommend(course_name):
        return Course.data[course_name].recommendation
