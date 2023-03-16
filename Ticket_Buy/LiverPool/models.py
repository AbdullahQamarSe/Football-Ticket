from django.db import models

# Create your models here.

class TicketDetail(models.Model):
    ticket = models.CharField(max_length=200, null=True)
    
    class Meta:
            verbose_name = "Ticket List"    