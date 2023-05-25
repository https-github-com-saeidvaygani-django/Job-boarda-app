from django.db import models
from django.utils import timezone


class ApplicantsTable(models.Model):
    applicants_id = models.AutoField(primary_key=True,verbose_name="Id")
    applicants_name = models.CharField(max_length=50,verbose_name="Name")
    applicants_born_date = models.DateField(auto_now_add=True, null=True, verbose_name="Born Date") 
    applicants_user_emaill = models.EmailField(verbose_name="Email",null=True,max_length= 100)
    applicants_password = models.CharField(max_length=12,verbose_name="Password")
    applicants_city = models.CharField(max_length=50, verbose_name="City")
    applicants_major = models.ForeignKey('MajorsTable', on_delete=models.CASCADE, null=True,default='', verbose_name="Major")
    applicants_interestedin = models.CharField(max_length=50, verbose_name="Interested in")
    applicants_resume = models.CharField(max_length=50, verbose_name="Resume")
    
    def __str__(self):
        return self.applicants_name 
    
class CompaniesTable(models.Model):
    companies_id = models.AutoField(primary_key=True, verbose_name="Id")
    companies_name = models.CharField(max_length=50, verbose_name="Name")
    companies_description = models.TextField(max_length=200, verbose_name="Company Description")
    companies_email = models.EmailField(max_length=100, verbose_name="Email")
    companies_password = models.CharField(max_length=12, verbose_name="Password")
    companies_telephone = models.CharField(max_length=25, verbose_name="Telephone")
    companies_website = models.CharField(max_length=50, verbose_name="Website")
    companies_jobneeds = models.ForeignKey('JobsTable', null=True, default='', on_delete=models.CASCADE, verbose_name="Job needs")
    companies_city = models.CharField(max_length=50, verbose_name="City")
    companies_salary = models.CharField(max_length=10, verbose_name="Salary")
    companies_Jobrequirement_description = models.TextField(max_length=200, verbose_name="Job Requirement Description")
    companies_applicantsid = models.ManyToManyField('ApplicantsTable',default='', verbose_name="Applicants Id")
    
    def __str__(self):
        return self.companies_name
    
class JobsTable(models.Model):
    jobs_id = models.AutoField(primary_key=True, verbose_name="Id")
    jobs_title = models.CharField(max_length=50, verbose_name="Job Title")
    jobs_description = models.TextField(max_length=200, verbose_name="Job Descriptions")
    jobs_requirements = models.TextField(max_length=200, verbose_name="Job Requirements")
    jobs_city = models.CharField(max_length=50, verbose_name="City")
    
    def __str__(self):
        return self.jobs_title
    
class MajorsTable(models.Model):
    majors_id = models.AutoField(primary_key=True, verbose_name="Id")
    majors_name = models.CharField(max_length=50, verbose_name="Major Name")
    
    def __str__(self):
        return self.majors_name
    