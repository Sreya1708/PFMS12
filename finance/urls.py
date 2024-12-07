from django.urls import path, include
from . import views

app_name = 'finance'


urlpatterns = [
    path('financeHomePage/', views.financeHomepage, name='financeHomePage'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('budget-alerts/', views.budget_alerts, name='budget_alerts'),
    path('goal_list/', views.goal_list, name='goal_list'),
    path('savings_tracker/', views.savings_tracker, name='savings_tracker'),
    path('settings/', views.settings_profile, name='settings_profile'),
    path('spending_analysis/', views.spending_analysis, name='spending_analysis'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('emi_calculator/', views.emi_calculator, name='emi_calculator'),

]