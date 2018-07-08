from django.db import models

# Creating table

class Books(models.Model):

    def __str__(self):
        return self.name + '-' +self.author
 
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

#another table
class table_name(models.Model):
    fiction = models.CharField(max_length=100)
    non_fiction = models.CharField(max_length=100)
