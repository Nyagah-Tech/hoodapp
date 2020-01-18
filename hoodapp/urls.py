from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('add/bussiness/',views.add_bussiness,name = 'add-bussiness'),
    path('new/post/',views.new_post,name = 'new-post'),
    path('profile/',views.profile,name="profile"),
    path('update/profile/',views.update_profile,name="update-profile"),
    path('logout/',views.logout_view,name="logout"),
    path('neighbourhood/<int:id>',views.location_view, name="location"),
    path('hospital/<int:id>',views.hospital_view,name='hospital'),
    path('business/<int:id>',views.business_view,name = 'business'),
    #dasboard
    path("dashboard/",views.dashboard, name="user_dashboard"),
    path("users/", views.registered_users,name = 'system_users'),
    path("user/activate/<int:user_id>",views.user_activate,name="activate_user"),
    path("user/deactivate/<int:user_id>",views.user_deactivate,name="deactivate_user"),
    
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)