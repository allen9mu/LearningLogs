#learning logs

from django.conf.urls import url

from learning_logs import views

urlpatterns = [
    #index 
    url(r'^$',views.index, name = 'index'),
    #show all topic
    url(r'^topics/$', views.topics,name = 'topics'),
    #show topic entry detail
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic,name = 'topic'),
    #add new topic
    url(r'^new_topic/$', views.new_topic,name = 'new_topic'),   
    #add new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,name = 'new_entry'),
    #edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name = 'edit_entry'),      
]