from django.db import models

# Create your models here.
class GymMemberDetails(models.Model):
    user_email = models.CharField()
    plan = models.CharField(max_length=20)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    final_billing = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"{self.user_email} - Details"
