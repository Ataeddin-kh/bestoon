from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^submit/Expense/$',views.submit_expense,name="submit_expense")

]
