from django.urls import path

from monitoring import views

urlpatterns = [
	path('',views.index, name='index'),
	path('dashboard/<int:dashbrd_id>/', views.dashboard_detail, name='Dashboard Detail'),
	path('dashboard/<int:dashbrd_id>/<host_id>/', views.host_detail, name='Host Detail'),
]