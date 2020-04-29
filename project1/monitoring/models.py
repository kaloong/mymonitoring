from django.db import models

# Create your models here.
class Dashboard(models.Model):
	name = models.CharField(max_length=60, unique=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class DashboardGroup(models.Model):
	group = models.ForeignKey( 'Group', on_delete=models.CASCADE , related_name="dashboard_group")
	dashboard = models.ForeignKey( 'Dashboard', on_delete=models.CASCADE, related_name="dashboard_dashboardgroup")
	
	class Meta:
		unique_together= ('dashboard','group')

	def __str__(self):
		return "%s-%s"%(self.dashboard,self.group)


class Group(models.Model):
	name = models.CharField(max_length=60, unique=True)
	code = models.CharField(max_length=60, blank=True)
	description = models.TextField(blank=True, null=True)
	groupprobe = models.ForeignKey( 'Probe', on_delete=models.CASCADE,null=True)
	groupdashboard = models.ManyToManyField( 'Dashboard', through='DashboardGroup')
	def __str__(self):
		return self.name

class Host(models.Model):
	name = models.CharField(max_length=60, unique=True)
	ipaddr = models.CharField(max_length=15, null=True, blank=True)
	description = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name	

class Status(models.Model):
	name = models.CharField(max_length=60, unique=True)
	description = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return self.name

class Probe(models.Model):
	name = models.CharField(max_length=60, unique=True)
	description = models.TextField(blank=True, null=True)
	path = models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.name



class HostStatus(models.Model):
	group = models.ForeignKey('Group', on_delete=models.CASCADE, default=1,)
	host = models.ForeignKey('Host', on_delete=models.CASCADE, )
	status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True,)
	def __str__(self): 
		return "%s-%s-%s"%(self.group,self.host,self.status)

#class ProbeHostStatus(models.Model):
#	group = models.ForeignKey('Group', on_delete=models.CASCADE, default=1, related_name="probe_group")
#	host = models.ForeignKey('Host', on_delete=models.CASCADE, related_name="probe_host")
#	probe = models.ForeignKey('Probe', on_delete=models.CASCADE, related_name="probe_probe")
#	status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True, related_name="probe_status")
#	def __str__(self): 
#		return "%s-%s-%s-%s"%(self.group,self.host,self.probe,self.status)