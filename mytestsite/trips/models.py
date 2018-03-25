from django.db import models
import re

class Course():
    """The model for a course."""

    data = {}

    def __init__(self, cid, title, description, class_type, instructor, recommendation):
        """ Initialize a Course recommendation """
        self.id = cid
        self.title = title
        self.description = description
        self.class_type = class_type
        self.instructor = instructor
        self.recommendation = recommendation

    @staticmethod
    def get_match(keyword):
        return [k for k, v in Course.data.items() if re.search(keyword, k, re.IGNORECASE)]

    @staticmethod
    def get_recommend_courses(course_name):
        """Get a dictionary of the course and their descriptions."""
        recs = Course.get_recommend(course_name)
        descriptions = {}
        instructors = {}
        class_types = {}
        for cname, value in recs.items():
            course = Course.data[cname]
            descriptions[cname] = course.description
            instructors[cname] = course.instructor
            class_types[cname] = course.class_type
        return recs, descriptions, instructors, class_types

    @staticmethod
    def get_recommend(course_name):
        return Course.data[course_name].recommendation
