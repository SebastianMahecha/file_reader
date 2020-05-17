from django.urls import path
from . import views

urlpatterns = [    
    path('reader/pdf/view', views.pdf_reader_view, name='pdf_reader_view'),
    path('reader/pdf/new/view', views.pdf_reader_new_view, name='pdf_reader_new_view'),
    path('reader/pdf/save', views.pdf_reader_save, name='pdf_reader_save'),
]

