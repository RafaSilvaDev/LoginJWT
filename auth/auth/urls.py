from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('api/v1', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]

'''
JWT TOKEN FOR ADMIN:
{
		"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MzgxMDM2MCwianRpIjoiOGRmOTQyN2I4OGIyNGE3OWJkNmI1YTU4MmY5NDkxNGMiLCJ1c2VyX2lkIjoxfQ.-2YnSG5BiDf8JCXvzfXDivcUSbqilQStEyBYM2em1DE",
	    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzI3NTYwLCJqdGkiOiI3MzcyNmExYWIzNmU0OWM4YmM3YTJmZjViNzRlZTI4YyIsInVzZXJfaWQiOjF9.qngOK_OsU_0r2pLG8JjbpEHYYIUZJgxso-fnRQVg3iE"
}
'''