from django.urls import path
from .views import ContactDetailedView,ContactList

urlpatterns = [
    path('',ContactList.as_view()),
    path('<int:id>',ContactDetailedView.as_view()),
]