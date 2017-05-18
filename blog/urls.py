from django.conf.urls import url
from . import views

#from django.views.generic.dates import ArchiveIndexView
#from blog.models import Article

urlpatterns = [
   
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/search/$', views.post_search, name='post_search'),

    #url(r'^archive/$', ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
    #    name="archive"),

    


    
]


'''
urlpatterns = [

 	 url(r'^$', views.post_list),
     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
     url(r'^post/new/$', views.post_new, name='post_new'),

   '''  

