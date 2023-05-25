import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from product.models import JobsTable

def import_data():
    file_path = 'file1.csv'  # Update with the path to your CSV file

    with open("file1.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            jobs_id, jobs_title, jobs_description, jobs_requirements, jobs_city = row
            
            # Print the record in the terminal
            print(f"Jobs ID: {jobs_id}")
            print(f"Title: {jobs_title}")
            print(f"Description: {jobs_description}")
            print(f"Requirements: {jobs_requirements}")
            print(f"City: {jobs_city}")
            print()  # Empty line for readability
            
            # Create a new JobsTable instance and save it to the database
            job = JobsTable(
                jobs_id=int(jobs_id),
                jobs_title=jobs_title,
                jobs_description=jobs_description,
                jobs_requirements=jobs_requirements,
                jobs_city=jobs_city
            )
            job.save()

if __name__ == '__main__':
    import_data()
