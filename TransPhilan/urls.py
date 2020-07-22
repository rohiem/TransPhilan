"""TransPhilan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as profileview

from pay import views as payview

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include("trans.urls")),
#    path('requests', profileview.homerequest, name='requests'),
#    path('requests/<int:id>', profileview.detail, name='detail'),
#    path('requests/<int:id>/upvote', profileview.upvote, name='upvote'),

#    path('profiles', profileview.Home, name='profiles'),
    path('about', profileview.about, name='about'),
#    path('profile', profileview.userProfile, name='profile'),
#    path('pay', payview.pay, name='pay'),
#    path('contact', contactview.Home, name='contact'),
#    path('index', contactview.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('', include('pay.urls')),
    path('profiles/<slug:slug>/createprofile',
         profileview.ProfileCreateView.as_view(), name="createprofile"),
    path('profiles/<slug:slug>', profileview.userProfile, name="profile"),
#    path('createrequest', profileview.RequestCreateView.as_view(), name="createrequest"),
#    path('vote/<int:pk>',profileview.ProductVoteToggle.as_view() , name="upvote"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)