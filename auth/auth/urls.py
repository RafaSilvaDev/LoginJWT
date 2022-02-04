from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('', include('login.urls')),
]

'''
JWT TOKEN FOR ADMIN:
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDA1OTIwMCwianRpIjoiODE1OGMyMmE5NjhmNGRhNGIxMmI1NjUwN2I1OTdhMWMiLCJ1c2VyX2lkIjoxfQ.JC7FEPcoOldEryBVvUjaGVuEtw7FXChEd1DiOv80Urg",

    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzOTgxNzc1LCJqdGkiOiI4Y2Y1ZTBjNTMxYWM0Zjk0Yjg1OTJlODA0ZDg2NDY5ZiIsInVzZXJfaWQiOjF9.YL8eYirvmR22ZFXF-vCqXeDMR-zUpUD-kf9VQTY9qks"
}
'''