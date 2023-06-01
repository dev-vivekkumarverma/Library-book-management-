from django.db import models
from userHandler.models import Student
from django.urls import reverse
# Create your models here.

class Connection(models.Model):
    requested_by=models.ForeignKey(Student,on_delete=models.DO_NOTHING,related_name="connection")
    requested_for=models.ForeignKey(Student,on_delete=models.DO_NOTHING,related_name="connections")
    is_approved=models.BooleanField(default=False)
    is_removed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.requested_by.roll_number} -> {self.requested_for.roll_number}"
    
    def get_apppoval_urls(self):
        return reverse("approve_connection_view",kwargs={"studentID":self.requested_for,"connectionID":self.pk})
