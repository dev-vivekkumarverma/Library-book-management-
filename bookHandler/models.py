from django.db import models
from userHandler.models import Student
from datetime import datetime

#  title, author, genre, year of publication, and ISBN stored in the database.

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100,null="True")
    genre=models.CharField(max_length=100,null="True")
    year_of_publication=models.CharField(max_length=4,null="True")
    ISBN=models.CharField(max_length=13,unique=True)

    def __str__(self) -> str:
        return self.title
    

class BookStatistics(models.Model):
    book=models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    total_units=models.IntegerField(default=0)
    total_used=models.IntegerField(default=0)
    def is_available(self):
        return (self.total_units > self.total_used)
    def total_available(self):
        return (self.total_units-self.total_used)
    def increase_total_used(self,units:int=1):
        if (self.total_used + units) <=self.total_units and units>0:
            self.total_used+=units
            self.save()
            return True
        return False
    def decrease_total_used(self,units:int=1):
        if units<=self.total_used and units>0:
            self.total_used-=units
            self.save()
            return True
        return False
        
    
class BookBorrowDetails(models.Model):
    book=models.ForeignKey(Book,on_delete=models.DO_NOTHING)
    student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    units=models.IntegerField(default=1)
    timestamp=models.DateTimeField(auto_now_add=True)
    total_number_of_days=models.IntegerField(default=15)
    submitted_at=models.DateTimeField(null=True, blank=True)
    is_fine_cleared=models.BooleanField(default=False)
    is_submitted=models.BooleanField(default=False)
    def is_fined(self):
        if (self.timestamp-datetime.now()).days>self.total_number_of_days:
            return True
        return False
    
    def total_fine(self, rate_per_day=5):
        if self.is_fined():
            total_fined_amount=((self.timestamp-datetime.now()).days-self.total_number_of_days)*rate_per_day
            return total_fined_amount
        return 0
    
    def submit_book(self):
        if self.is_submitted==False:
            self.is_submitted=True
            self.submitted_at=datetime.now()
            self.save()
            
    def unsubmit_book(self):
        if self.is_submitted==True:
            self.is_submitted=False
            self.submitted_at=""
            self.save()
            
    
    def clear_fine(self):
        self.is_fine_cleared=True
        self.save()
        return True
