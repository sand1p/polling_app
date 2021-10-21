from django.urls import include, path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
    path('get_latests/<int:hour>/', views.get_latest_snippets)
]
urlpatterns = format_suffix_patterns(urlpatterns)
