from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'category', 'amount', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter expense name'}),
            'category': forms.Select(choices=[
                ('', 'Select category'),
                ('Food', 'Food'),
                ('Transportation', 'Transportation'),
                ('Utilities', 'Utilities'),
                ('Entertainment', 'Entertainment'),
                ('Healthcare', 'Healthcare'),
                ('Other', 'Other')
            ]),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }



from django import forms
from .models import BudgetAlert

class BudgetAlertForm(forms.ModelForm):
    class Meta:
        model = BudgetAlert
        fields = ['monthly_budget', 'alert_threshold']
        widgets = {
            'monthly_budget': forms.NumberInput(attrs={'placeholder': 'Enter your monthly budget'}),
            'alert_threshold': forms.NumberInput(attrs={'placeholder': 'Enter alert threshold %'}),
        }


from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'amount', 'deadline', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Save for a car'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter the amount', 'min': 0}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your goal'})
        }



from django import forms
from .models import SavingsEntry

class SavingsEntryForm(forms.ModelForm):
    class Meta:
        model = SavingsEntry
        fields = ['goal', 'saved', 'description']
        widgets = {
            'goal': forms.NumberInput(attrs={'placeholder': 'Enter your savings goal', 'min': 0}),
            'saved': forms.NumberInput(attrs={'placeholder': 'Enter the amount saved so far', 'min': 0}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your savings plan'}),
        }



from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'monthly_budget', 'preferred_currency']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'monthly_budget': forms.NumberInput(attrs={'placeholder': 'Your budget'}),
            'preferred_currency': forms.Select(),
        }

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Current password'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}))

from django import forms
from .models import Spending

class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ['category', 'amount']
        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'Enter category'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
        }

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']