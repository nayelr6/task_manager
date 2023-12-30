from django.urls import path
from .views import user_registration_view, user_login_view, get_user_info_view, update_user_profile, delete_user,user_logout
from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns = [
#     path('register/', UserRegistrationAPIView.as_view(), name='register'),
#     path('login/', UserLoginAPIView.as_view(), name='login'),
# ]


urlpatterns = [
    
    path('register/',user_registration_view, name='register'),
    path('login/',user_login_view,name= 'user_login'),
    path('get-user-info/', get_user_info_view, name='get_user_info'),
    path('update-profile/', update_user_profile, name='update_user_profile'),
    path('delete/', delete_user, name='delete_user'),
    path('logout/', user_logout, name='user_logout'),
]
