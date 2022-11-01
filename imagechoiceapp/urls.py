from django.urls import path
from . import views
from .views import IndexView, ChoiceView

app_name = 'imagechoiceapp'

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:quantity>/', ChoiceView.as_view()),
    ]
