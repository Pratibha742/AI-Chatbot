from django.urls import path
# from .views import chat_view,chat_page,landing_page
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.landing_page, name = 'landing_page'),
    path('register/',views.register, name = 'register'),
    path('login/',views.CustomLoginView.as_view(), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page = 'login'), name = 'logout'),
    # path('chat/',views.chat_redirect_required, name = 'chat_redirect'),
    path('chat/',views.chat_page, name = 'chat_page'),
    # path('chat/', views.chat_page_default, name='chat_page_default'),
    path('api/chat/',views.chat_view,name = 'chat_view'),
]
