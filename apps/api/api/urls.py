from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('api/validate_mfa_code/', views.validate_mfa_code, name='validate_mfa_code'),
    path('api/generate_mfa_code/', views.generate_mfa_code, name='generate_mfa_code'),
]

urlpatterns += [
    path('api/enable_mfa/', views.enable_mfa, name='enable_mfa'),
    path('api/mfa_setup/', views.mfa_setup, name='mfa_setup'),
    path('api/disable_mfa/', views.disable_mfa, name='disable_mfa'),
    path('api/disable_mfa_confirm/', views.disable_mfa_confirm, name='disable_mfa_confirm'),
    path('api/mfa_recovery/', views.mfa_recovery, name='mfa_recovery'),
    path('api/mfa_recovery_instructions/', views.mfa_recovery_instructions, name='mfa_recovery_instructions'),
    path('api/enforce_mfa/', views.enforce_mfa, name='enforce_mfa'),
    path('api/protected_view/', views.protected_view, name='protected_view'),
    path('api/verify_mfa/', views.verify_mfa, name='verify_mfa'),
    path('api/generate_mfa_secret/', views.generate_mfa_secret, name='generate_mfa_secret'),
]