from django.db import models

# Create your models here.
# n Django applications, the models.py file is used to define the data models for your application. 
# These models represent the structure of the data that your application will work with, including the 
# tables in your database (if you're using a relational database like SQLite, PostgreSQL, MySQL, etc.).

# Here's what you typically do in a models.py file:

# Define Django Models: You define Python classes that subclass django.db.models.Model. Each class represents a table in your database, and each attribute of the class represents a field in that table. Django provides various field types (e.g., CharField, IntegerField, DateTimeField, etc.) to represent different types of data.

# python
# Copy code
# from django.db import models

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField()
#     date_created = models.DateTimeField(auto_now_add=True)
# Run Migrations: After defining your models, you need to create migrations, which are Python files that define the changes to your database schema. You can create migrations using the makemigrations command:

# bash
# Copy code
# python manage.py makemigrations
# This command analyzes your models and creates migration files in the migrations directory of your app.

# Apply Migrations: Once you've created migrations, you apply them to your database using the migrate command:

# bash
# Copy code
# python manage.py migrate
# This command runs the migrations and updates your database schema accordingly.

# Interact with Data: Once your models are defined and migrations are applied, you can interact with your data using Django's ORM (Object-Relational Mapping). You can create, read, update, and delete objects using Python code, and Django handles the underlying database operations for you.

# The models.py file is a fundamental part of Django applications as it defines the data structure of your application and provides a convenient way to work with databases.


class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 225 )
    price = models.FloatField()
    description = models.TextField
    count = models.IntegerField()
    is_active = models.BooleanField() 


class Category(models.Model):
    name = models.CharField(max_length = 255) 



