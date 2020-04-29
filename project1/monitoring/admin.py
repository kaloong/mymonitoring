from django.contrib import admin
from monitoring.models import Dashboard,DashboardGroup,Group,Probe,Host,Status,HostGroup


# Register your models here.
admin.site.site_header="My Monitoring"

class HostGroupAdmin(admin.ModelAdmin):
	list_display=['group','host']
	save_as = True

class HostGroupInline(admin.TabularInline):
	model = HostGroup
	extra = 2 

class GroupAdmin(admin.ModelAdmin):
	list_display = ('name','code','groupprobe')
	fieldsets = \
	[ 
	('Group name',{'fields':['name']} ),
	('Code name', {'fields':['code']} ),  
	('Group probe', {'fields':['groupprobe']} ),  
	]
	inlines = [HostGroupInline]
	ordering = ['name']

class GroupInline(admin.StackedInline):
	model = Group
	extra = 4

class DashboardInline(admin.TabularInline):
	model = Dashboard
	extra = 4 

class DashboardAdmin(admin.ModelAdmin):
	list_display = ['name','description']

class DashboardGroupInline(admin.TabularInline):
	model = DashboardGroup
	extra = 2

class DashboardGroupAdmin(admin.ModelAdmin):
	pass


class ProbeAdmin(admin.ModelAdmin):
	pass

class HostInline(admin.TabularInline):
	pass

class HostAdmin(admin.ModelAdmin):
	pass

class StatusAdmin(admin.ModelAdmin):
	pass

admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(DashboardGroup, DashboardGroupAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Probe, ProbeAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
