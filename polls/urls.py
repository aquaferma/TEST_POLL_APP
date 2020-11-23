from django.urls import path, include
from polls import views

urlpatterns = [
    path("auth/", include('rest_framework.urls')),
    path("polls/", views.PollsView.as_view()),
    path("pass/", views.UserChoiceView.as_view()),
]