from django.db import models


class Course():
    """The model for a course."""

    data = {}

    def __init__(self, cid, title, description, rating, class_type, 
                 instructor, tid, recommendation):
        """ Initialize a Course recommendation """
        self.id = cid
        self.title = title
        self.description = description
        self.rating = rating
        self.class_type = class_type
        self.instructor = instructor
        self.tid = tid
        self.recommendation = recommendation

    @staticmethod
    def get_match(keyword):
        return [k for k, v in Course.data.items() if keyword in k]

    @staticmethod
    def get_recommend_courses(course_name):
        """Get a dictionary of the course and their descriptions."""
        recs = Course.get_recommend(course_name)
        return [Course.data[cname] for cname, _ in recs.items()]

    @staticmethod
    def get_recommend(course_name):
        return Course.data[course_name].recommendation
