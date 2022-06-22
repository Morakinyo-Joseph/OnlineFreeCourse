from django.db import models
from datetime import datetime
#
#Note from FIFE: Lecturers should have a one to many attribute... Django has a constraint for that I guess
#
# class TeacherModel():
#     #
#     # GENDER_CHOICES = (
#     #     ("male", "Male"),
#     #     ("female", "Female")
#     # )
#     #
#     # first_name = models.CharField(max_length=30)
#     # last_name = models.CharField(max_length=30)
#     # email = models.EmailField(max_length=30)
#     # password = models.CharField(max_length=30)
#     #
#     # date_of_birth = models.DateField(null=False)
#     # gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
#     #
#     # registration_date = models.DateTimeField(default=datetime.now)
#     #
#     # def __str__(self):
#     #     return self.email
#
