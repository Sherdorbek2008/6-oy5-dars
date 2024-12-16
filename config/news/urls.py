from django.urls import path
from .views import index,post_by_curses
urlpatterns = [
    path('',index),
    path('course/<int:course_id>/',post_by_curses,name=post_by_curses)
]