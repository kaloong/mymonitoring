from django.shortcuts import render, get_object_or_404, get_list_or_404
#from django.http import HttpResponse
#from django.template import loader
from monitoring.models import DashboardGroup, Dashboard, Group, Host
# Create your views here.
def index(request):
	dashboard_list=Dashboard.objects.order_by('name')
	context = { 'dashboard_list' : dashboard_list,}
	return render( request, 'monitoring/index.html', context)
	#template = loader.get_template('monitoring/index.html')

	#context = { 'dashboard_list' : dashboard_list,}
	#return HttpResponse( template.render(context, request ))

#def dashboard_groups(request):
#	dashboard_list=Group.objects.order_by('name')
#	context = { 'dashboard_list' : dashboard_list,}
#	return render( request, 'monitoring/index.html', context)

def dashboard_detail( request, dashbrd_id):
	#groups_list =  DashboardGroup.objects.filter(dashboard_id=dashbrd_id ) 
	dashboard = get_object_or_404( Dashboard, pk=dashbrd_id )
	groups_list = Group.objects.filter(groupdashboard=dashbrd_id)
	groups = groups_list.all()
	#groups = ', '.join( [ group.name for group in groups_list.filter(pk=dashboard_id) ])
	context = { 'dashboard': dashboard , 'groups': groups }
	return render( request, 'monitoring/dashboard_detail.html', context )

def host_detail( request, dashbrd_id, host_id):
	host = get_object_or_404( Host, id=host_id)
	context = { 'host': host }
	return render( request, 'monitoring/host_detail.html',context)