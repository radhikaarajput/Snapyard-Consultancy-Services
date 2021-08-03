from django.urls import path
from . import views
urlpatterns = [

    path("",views.index,name='index'),
    path('plant/', views.plant, name='plant'),
    path('flowers/', views.flowers, name='flowers'),
    path('subscription/', views.subscription, name='subscription'),
    path('shantiCafe/', views.shantiCafe, name='shantiCafe'),
    path('blog/', views.blog, name='blog'),
    path('ourStory/', views.ourStory, name='ourStory'),
    path('contact/', views.contact, name='contact'),
    path('beSpoke/', views.beSpoke, name='beSpoke'),
]