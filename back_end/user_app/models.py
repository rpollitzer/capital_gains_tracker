from django.db import models
from django.contrib.auth.models import AbstractUser


class User_app(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null= True)
    # filling_status will be a forced choice between 3 options on front end
    filing_status = models.CharField(max_length=100, null=True)
    #how much does the user make from other sources 
    estimated_year_income = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    # Anything over 1 year
    long_term_gains = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    # Anything under 1year
    short_term_gains = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    # inital investment
    contributed_capital = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    losses = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.email