from django.urls import include, path
from django.views.generic import TemplateView
from user.views import GetAllUsers, GetIncomeByID, UserIncome, UserExpenditure, GetExpenditureByID


urlpatterns = [
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    path("", GetAllUsers.as_view(), name=""),
    path("income/", UserIncome.as_view(), name="income"),
    path("income/<str:pk>/", GetIncomeByID.as_view(), name="income/incomeID"),
    path("expenditure/", UserExpenditure.as_view(), name="expenditure"),
    path("expenditure/<str:pk>/", GetExpenditureByID.as_view(), name="expenditure/expenditureID"),
    # path('swagger/', include('user.swagger')),

]