from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index, name='index'),
   # path('home/', views.home, name='home'),
   # path('topic-listing/', views.topic_listing, name='topic_listing'),
   # path('topic-detail/', views.topic_detail, name='topic_detail'),
   # path('contact/', views.contact, name='contact'),
    path('', views.finance_topic_detail, name='finance_topic_detail'),
    path('finance-topic-detail/', views.finance_topic_detail, name='finance_topic_detail'),
    path('finance-topic-onecolumn/', views.finance_topic_onecolumn, name='finance_topic_onecolumn'),
    path('finance-topic-twocolumn/', views.finance_topic_twocolumn, name='finance_topic_twocolumn'),
    path('finance-topic-twocolumnset/', views.finance_topic_twocolumnset, name='finance_topic_twocolumnset'),
    path('finance-topic-threecolumn/', views.finance_topic_threecolumn, name='finance_topic_threecolumn'),
]
