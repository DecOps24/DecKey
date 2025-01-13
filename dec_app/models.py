from datetime import date

from django.db import models

# Create your models here.



class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=10,default = 000)

    def __str__(self):
        return self.staff_name



class Party(models.Model):
    Party_name = models.CharField(max_length=50,unique=True)
    party_phone_number = models.CharField(max_length=10,default= 0000000000)
    party_address = models.CharField(max_length=100)
    referance = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.Party_name



class Work_Details(models.Model):
    sts = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('cancelled', 'cancelled'),
    )


    Party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    Nature_of_work = models.CharField(max_length=255)
    Assigned_to = models.ForeignKey(Staff,on_delete=models.CASCADE)
    Details = models.CharField(max_length=255)
    Status = models.CharField(max_length=255,choices=sts,default='Pending')
    Finished_date = models.DateField(null=True,blank=True)
    Delivery_Date = models.DateField(null=True,blank=True)
    Bill_Amount = models.CharField(max_length=255,null=True,blank=True)
    Fee_amount = models.CharField(max_length=255,null=True,blank=True)
    DOR = models.DateField(default=date.today)
