from django.urls import path

from monitoring import views

urlpatterns = [
	path('',views.index, name='index'),
	path('dashboard/<int:dashbrd_id>/', views.dashboard_detail, name='dashboard_detail'),
	path('dashboard/<int:dashbrd_id>/<host_id>/', views.host_detail, name='host_detail'),
	path('dashboard/run_task/<host_id>', views.run_task, name='run_task'),
]