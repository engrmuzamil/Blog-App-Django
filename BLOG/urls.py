from django.urls import path
from .views import homeview, detailview
urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('detail/<int:pk>/', detailview.as_view(), name="detailview"),

]
