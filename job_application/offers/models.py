from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True,blank=True)
    street = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.company_name

class Site(models.Model):
     site = models.CharField(max_length=100,null=True,blank=True)
     def __str__(self):
         return self.site

class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    telephone = models.IntegerField(null=True,blank=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.surname

class Offer(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    job_number = models.CharField(max_length=100,null=True,blank=True)
    benefits = models.TextField()
    salary_expectation = models.CharField(max_length=20,null=True,blank=True)
    added_date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=500,null=True,blank=True)
    offer_file = models.FileField(upload_to='media/offers/offers/',blank=True)
    cv = models.FileField(upload_to='media/offers/cv/',blank=True)
    contact_person = models.ForeignKey(Person,on_delete=models.CASCADE, null=True,blank=True)
    send_date = models.DateField()
    site = models.ForeignKey(Site,on_delete=models.CASCADE)

    def __str__(self):
        return self.company.company_name + ' ' + self.title