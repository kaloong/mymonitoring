from django.urls import path

from monitoring import views

urlpatterns = [
	path('',views.index, name='index'),
	path('dashboard/<int:dashbrd_id>/', views.dashboard_detail, name='Dashboard Detail'),
]