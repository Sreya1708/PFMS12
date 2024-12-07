from django.shortcuts import render

# Create your views here.
def financeHomepage(request):
    return render(request,'finance/financeHomePage.html')

from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    expenses = Expense.objects.all()
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'finance/expense_tracking.html', {'form': form, 'expenses': expenses})


# Create your views here.



from django.shortcuts import render, redirect
from .models import BudgetAlert
from .forms import BudgetAlertForm

def budget_alerts(request):
    if request.method == "POST":
        form = BudgetAlertForm(request.POST)
        if form.is_valid():
            budget_alert = form.save(commit=False)
            budget_alert.user = request.user
            budget_alert.save()
            return redirect('finance:budget_alerts')
    else:
        form = BudgetAlertForm()

    return render(request, 'finance/budget_alerts.html', {'form': form})



from django.shortcuts import render, redirect
from .models import Goal
from .forms import GoalForm


def goal_list(request):
    goals = Goal.objects.all()
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:goal_list')
    else:
        form = GoalForm()

    return render(request, 'finance/goal_setting.html', {'form': form, 'goals': goals})



from django.shortcuts import render, redirect
from .models import SavingsEntry
from .forms import SavingsEntryForm


def savings_tracker(request):
    savings_entries = SavingsEntry.objects.all()
    if request.method == "POST":
        form = SavingsEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:savings_tracker')
    else:
        form = SavingsEntryForm()

    return render(request, 'finance/savings_tracker.html', {'form': form, 'savings_entries': savings_entries})

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, PasswordChangeForm

@login_required
def settings_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        password_form = PasswordChangeForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
        if password_form.is_valid():
            current_password = password_form.cleaned_data.get('current_password')
            new_password = password_form.cleaned_data.get('new_password')
            confirm_password = password_form.cleaned_data.get('confirm_password')
            if not request.user.check_password(current_password):
                messages.error(request, 'Current password is incorrect.')
            elif new_password != confirm_password:
                messages.error(request, 'New passwords do not match.')
            else:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Important for keeping the user logged in
                messages.success(request, 'Password changed successfully!')
        return redirect('finance:settings_profile')
    else:
        profile_form = UserProfileForm(instance=user_profile)
        password_form = PasswordChangeForm()

    return render(request, 'finance/settings_profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


from django.shortcuts import render, redirect
from .models import Spending
from .forms import SpendingForm


def spending_analysis(request):
    spendings = Spending.objects.all()
    if request.method == "POST":
        form = SpendingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:spending_analysis')
    else:
        form = SpendingForm()

    return render(request, 'finance/spending_analysis.html', {'form': form, 'spendings': spendings})

from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'finance/add_task.html',
                  {'form' : form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('finance:add_task')

def calculatorpagecall(request):
    return render(request, 'finance/emi_calculator.html')

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

        return render(request, 'finance/emi_calculator.html', {'result': result})
    return render(request, 'finance/emi_calculator.html')


from django.shortcuts import render
from django.http import JsonResponse
import math


def emi_calculator(request):
    if request.method == "POST":
        # Extracting input values
        principal = float(request.POST.get('principal', 0))
        annual_rate = float(request.POST.get('rate', 0))
        tenure = int(request.POST.get('tenure', 0))

        if principal <= 0 or annual_rate <= 0 or tenure <= 0:
            return JsonResponse({"error": "Invalid input values"}, status=400)

        # EMI Calculation
        monthly_rate = annual_rate / (12 * 100)
        emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure)) / \
              (math.pow(1 + monthly_rate, tenure) - 1)

        return JsonResponse({"emi": round(emi, 2)})

    return render(request, "finance/emi_calculator.html")

