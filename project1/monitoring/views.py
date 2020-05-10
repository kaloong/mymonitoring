from django.shortcuts import render, get_object_or_404, get_list_or_404,HttpResponseRedirect
from monitoring.models import DashboardGroup, Dashboard, Group, Host
from django.views.generic.detail import DetailView
#from django.http import HttpResponse
#from django.template import loader

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
	dashboard_list=Dashboard.objects.order_by('name')
	#groups_list =  DashboardGroup.objects.filter(dashboard_id=dashbrd_id ) 
	dashboard = get_object_or_404( Dashboard, pk=dashbrd_id )
	groups_list = Group.objects.filter(groupdashboard=dashbrd_id)
	groups = groups_list.all()
	#groups = ', '.join( [ group.name for group in groups_list.filter(pk=dashboard_id) ])
	context = { 'dashboard_list': dashboard_list, 'dashboard': dashboard , 'groups': groups }
	return render( request, 'monitoring/dashboard_detail.html', context )


def host_detail( request, dashbrd_id, host_id):
	if request.method == 'GET' :
		dashboard_list=Dashboard.objects.order_by('name')
		host = get_object_or_404( Host, id=host_id)
		context = { 'dashboard_list': dashboard_list,'host': host, 'prev_page':request.META['HTTP_REFERER'] }
		return render( request, 'monitoring/host_detail.html',context)
	else:
		print("---")
		pass
		return HttpResponseRedirect(request.META['HTTP_REFERER'])

def run_task( request, host_id):
	host = get_object_or_404( Host, id=host_id)
	print("---- {} {}".format(host.id, host.name))
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

class host_detail_view( DetailView):
	model = Host
	template_name = 'monitoring/host_detail.html'
