from django.db import models

# Create your models here.

STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Bachelor in Science','Bachelor in Science'),
 ('Bachelor in ARTS','Bachelor in ARTS'),
 ('Bachelor in techlogy','Bachelor in techlogy'),
 ('Master in science','Master in science'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)

class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city =models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='my_file',blank=True)

GRADUATIONS_COURSE = (
 ('Bachelor in techlogy','Bachelor in techlogy'),
 ('Bachelor in Science','Bachelor in Science'),
 ('Bachelor in ARTS','Bachelor in ARTS'),
 ('Bachelor of Computer Applications','Bachelor of Computer Applications'),
 ('Bachelor of Business Administration','Bachelor of Business Administration'),
 ('Master in techlogy','Master in techlogy'),
 ('Master in science','Master in science')
)
#class Educ(models.Model):
#   objectives=models.CharField(max_length=500)
#    skills=models.CharField(max_length=500)
#    gratuation=models.CharField(choice=GRADUATIONS_COURSE,max_length=100)
#    secondary=models.CharField(max_length=500)
#    high_school=models.CharField(max_length=500)
#    percentage=models.IntegerField()
#    projects=models.CharField(max_length=500)
    