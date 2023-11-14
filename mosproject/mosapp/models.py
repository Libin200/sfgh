from django.db import models

# Create your models here.
class register(models.Model):
    employee_id=models.IntegerField(null=False,unique=True)
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    contact=models.BigIntegerField()
    class Meta:
        db_table='register'
class email(models.Model):
    employee_id=models.IntegerField(null=False,unique=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    salary=models.IntegerField()
    
    class Meta:
        db_table='email'