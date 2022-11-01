from django.contrib import admin
from django.urls import include, path
from imagechoiceapp import views
from imagechoiceapp.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('imagechoiceapp/', include('imagechoiceapp.urls')),
]
