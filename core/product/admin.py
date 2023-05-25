from django.contrib import admin
from .models import ApplicantsTable,CompaniesTable,JobsTable,MajorsTable
from django.db import models


class ApplicantsTableAdmin(admin.ModelAdmin):
    list_display = ('applicants_id','applicants_name','applicants_born_date','applicants_user_emaill','applicants_city','applicants_major','applicants_interestedin')
    list_display_links = ('applicants_id','applicants_name','applicants_born_date','applicants_user_emaill','applicants_city','applicants_major','applicants_interestedin')
    list_filter = ('applicants_name','applicants_city')
    search_fields = ('applicants_name',)
    sortable_by = ('applicants_name',)
    ordering = ('applicants_id',)
    date_hierarchy = 'applicants_born_date'


class CompaniesTableAdmin(admin.ModelAdmin):
    list_display = ('companies_id','companies_name','companies_description','companies_email','companies_telephone','companies_website','companies_jobneeds','companies_city','companies_salary','companies_Jobrequirement_description')
    list_display_links = ('companies_id','companies_name','companies_description','companies_email','companies_telephone','companies_website','companies_jobneeds','companies_city','companies_salary','companies_Jobrequirement_description')
    list_filter = ('companies_name','companies_city')
    search_fields = ('companies_name',)
    sortable_by = ('companies_id',)
    ordering = ('companies_name',)


class JobsTableAdmin(admin.ModelAdmin):
    list_display = ('jobs_id','jobs_title','jobs_description','jobs_requirements','jobs_city')
    list_display_links = ('jobs_id','jobs_title','jobs_description','jobs_requirements','jobs_city')
    list_filter = ('jobs_city',)
    search_fields = ('jobs_title',)
    sortable_by = ('jobs_id',)
    ordering = ('jobs_title',)
    

class MajorsTableAdmin(admin.ModelAdmin):
    list_display = ('majors_id','majors_name')
    list_display_links = ('majors_id','majors_name')
    list_filter = ('majors_name',)

admin.site.register(ApplicantsTable,ApplicantsTableAdmin)
admin.site.register(CompaniesTable,CompaniesTableAdmin)
admin.site.register(JobsTable,JobsTableAdmin)
admin.site.register(MajorsTable,MajorsTableAdmin)