from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import archiveIndexView,YearArchiveView,MonthArchiveView,DayArchiveView,TodayArchiveView
from blog.models import Post
# Create your views here.
#- ListView

class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = 'posts'
    paginate_by = 2
# - DetailView
class PostDV(DetailView):
    model = Post
#--- ArchiveView
class PostAV(archiveIndexView):
    model = Post
    date_field = "modify_dt"
    make_object_list = True 
class PostYAV(YearArchiveView):
    model = Post
    date_field = "modify_dt"
    make_object_list= True
class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_dt"
    # make_object_list= True
class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_dt"
    # make_object_list= True
class PostDAV(DayArchiveView):
    model= Post  
    date_field= "modify_dt"
class PostTAV(TodayArchiveView):
    model =Post 
    date_field= 'modify_dt'


