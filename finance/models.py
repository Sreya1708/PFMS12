from django.db import models

# Create your models here.


from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def _str_(self):
        return f"{self.name} - {self.category} - ${self.amount} on {self.date}"


from django.db import models
from django.contrib.auth.models import User

class BudgetAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2)
    alert_threshold = models.PositiveIntegerField()  # Percentage

    def _str_(self):
        return f"{self.user.username} - Budget: ${self.monthly_budget}, Threshold: {self.alert_threshold}%"


from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.title


from django.db import models

class SavingsEntry(models.Model):
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    saved = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"Goal: ${self.goal}, Saved: ${self.saved}"



from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    preferred_currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('INR', 'INR'), ('GBP', 'GBP')], default='USD')

    def _str_(self):
        return self.user.username

from django.db import models

class Spending(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.category}: ${self.amount}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title