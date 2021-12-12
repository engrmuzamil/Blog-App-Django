from django.urls import path
from .views import homeview, detailview, newview, editview, deleteview
urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('detail/<int:pk>/', detailview.as_view(), name="detailview"),
    path('newview/', newview.as_view(), name='newview'),
    path('edit/<int:pk>/', editview.as_view(), name='edit'),
    path('delete/<int:pk>/', deleteview.as_view(), name="delete"),

]
