from django.urls import path
from . import views

urlpatterns=[
    # ex: /polls/index
    path('index/',views.index),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    #ex. /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # e.g. /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #e.g. /polls
    path('questions/', views.retrive_questions, name='show questions'),
]