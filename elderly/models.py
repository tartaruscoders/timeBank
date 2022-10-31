from django.db import models
from django.contrib.auth.models import User

# class Elder(models.Model):
#     # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     TITLES = (
#         ('Mr', 'Mister'),
#         ('Mrs', 'Miss'),
#         ('Ms', 'Mister'),
#         ('Miss', 'Miss'),
#         ('Dr', 'Dr.'),
#         ('Prof', 'Prof.'),
#     )
#     initials = models.CharField(max_length=3, choices=TITLES)
#     firstName = models.CharField(max_length=250)
#     lastName = models.CharField(max_length=300)
#     dateOfBirth = models.DateTimeField()
#     address = models.CharField(max_length=400)
#     phoneNumber = models.CharField(max_length = 10)

#     def __str__(self):
#         return str(self.user)

# # class Account_info(models.Model):
# #     AccountNo = models.IntegerField(primary_key=True)
# #     Owner = models.ForeignKey(Elder, on_delete=models.CASCADE)


