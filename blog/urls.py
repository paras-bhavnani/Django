from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('blogs/', views.blogs),
    path('blogger/<int:userId>', views.blogger, name='userId'),
    path('<int:blogId>', views.blogID, name='blogId'),
    path('bloggers/', views.bloggers),
]