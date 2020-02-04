from django.db import models


class Course(models.Model):
    course_id =                 models.IntegerField()
    course_name =               models.TextField()
    course_approval_score =     models.IntegerField(default=70)
    course_description =        models.TextField()
    course_availability =       models.BooleanField()

    def __str__(self):
        return self.content or ""


