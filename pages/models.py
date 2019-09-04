from django.db import models
from django.utils.timezone import now

#old model , to be deleted in cleanup
class List_mtd(models.Model):
	access_token=models.CharField(max_length=200)
	access_code=models.CharField(max_length=200)
	refresh_token=models.CharField(max_length=200)
	scope=models.CharField(max_length=200)
	endpoint=models.CharField(max_length=200)
	vrn=models.CharField(max_length=200)
	userid=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	src_sys_id=models.CharField(max_length=20)
	created_date = models.DateTimeField(default=now, editable=False)

#used for access token and refresh token
class mtd_tokens(models.Model):
	access_token=models.CharField(max_length=200)
	access_code=models.CharField(max_length=200)
	refresh_token=models.CharField(max_length=200)
	scope=models.CharField(max_length=200)
	endpoint=models.CharField(max_length=200)
	vrn=models.CharField(max_length=200)
	userid=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	src_sys_id=models.CharField(max_length=20)
	created_date = models.DateTimeField(default=now, editable=False)



#new users saved here  with endpoints
class testuser(models.Model):
	endpoint=models.CharField(max_length=200)
	vrn=models.CharField(max_length=200)
	userid=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	userFullName=models.CharField(max_length=200)
	emailAddress=models.CharField(max_length=200)
	created_date = models.DateTimeField(default=now, editable=False)
	src_sys_id=models.CharField(max_length=20)
	appname=models.CharField(max_length=20)

class auth_users(models.Model):
	agentarn=models.CharField(max_length=20)
	userid=models.CharField(max_length=20)
	planet=models.CharField(max_length=20)
	name=models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	service = models.CharField(max_length=20)
	clienttype=models.CharField(max_length=20)
	clientidtype=models.CharField(max_length=20)
	clientid=models.CharField(max_length=20)
	knownfact=models.CharField(max_length=20)
	created_date = models.DateTimeField(default=now, editable=False)
	src_sys_id=models.CharField(max_length=20)
	status=models.CharField(max_length=20)

	class Meta:
		managed= True		
	
	

#posted Vat returns model, and if successful, last few attributes store response return parameters from Vatpost
class posted(models.Model):
	periodKey=models.CharField(max_length=200)
	vatDueSales=models.CharField(max_length=200)
	vatDueAcquisitions=models.CharField(max_length=200)
	vatReclaimedCurrPeriod=models.CharField(max_length=200)
	netVatDue=models.CharField(max_length=200)
	totalValueSalesExVAT=models.CharField(max_length=200)
	totalValuePurchasesExVAT=models.CharField(max_length=200)
	totalValueGoodsSuppliedExVAT=models.CharField(max_length=200)
	totalAcquisitionsExVAT=models.CharField(max_length=200)
	finalised=models.CharField(max_length=200)
	vrn=models.CharField(max_length=200)
	date=models.CharField(max_length=200)
	access_token=models.CharField(max_length=200)
	endpoint=models.CharField(max_length=200)

#lists the apps created in hmrc sandbox with credentials , multiple to resolve errors in accessing
#hmrc if caused by throttlling
#uopdated by view initx.py

class apps_ids(models.Model):
	appname=models.CharField(max_length=200)
	client_Secrets=models.CharField(max_length=200)
	client_id=models.CharField(max_length=200)
	server_token=models.CharField(max_length=200)
	created_date = models.DateTimeField(default=now, editable=False)
	src_sys_id=models.CharField(max_length=20)
	

 #all views should log something
 #field names will be updated once we have something
class log1(models.Model):
	status1=models.CharField(max_length=200)
	status2=models.CharField(max_length=200)
	status3=models.CharField(max_length=2000)
	status4=models.CharField(max_length=2000)
	status5=models.CharField(max_length=200)
	status6=models.CharField(max_length=200)
	src_sys_id=models.CharField(max_length=20)
	created_date = models.DateTimeField(default=now, editable=False)


class pm(models.Model):
	sprint=models.CharField(max_length=200)
	description=models.CharField(max_length=2000)
	asignee=models.CharField(max_length=200)
	status=models.CharField(max_length=20)
	epic=models.CharField(max_length=100)
	priority = models.CharField(max_length=200)
	estimation = models.CharField(max_length=20)
	status2=models.CharField(max_length=200)
	status3=models.CharField(max_length=200)
	status4=models.CharField(max_length=200)
	status5=models.CharField(max_length=200)
	src_sys_id=models.CharField(max_length=200)
	completed=models.BooleanField(default=False)


	def __str__(self):
		return self.item + ' | ' + str(self.completed)

class pm2(models.Model):
	sprint=models.CharField(max_length=200)
	description=models.CharField(max_length=2000)
	asignee=models.CharField(max_length=200)
	status=models.CharField(max_length=20)
	epic=models.CharField(max_length=100)
	priority = models.CharField(max_length=200)
	estimation = models.CharField(max_length=20)
	status2=models.CharField(max_length=200)
	status3=models.CharField(max_length=200)
	status4=models.CharField(max_length=200)
	status5=models.CharField(max_length=200)
	src_sys_id=models.CharField(max_length=200)
	completed=models.BooleanField(default=False)


	def __str__(self):
		return self.item + ' | ' + str(self.completed)


class invoice(models.Model):
	invoice_ref_num = models.CharField(max_length=255, default=None, null=True)
	date = models.CharField(max_length=200, default=None, null=True)
	reference = models.CharField(max_length=200, default=None, null=True)
	account = models.CharField(max_length=200, default=None, null=True)
	client_name = models.CharField(max_length=200, default=None, null=True)
	address = models.CharField(max_length=200, default=None, null=True)
	invoice_version = models.CharField(max_length = 255, default=None, null=True)
	net = models.FloatField(default=0, null=True)
	gross = models.FloatField(default=0, null=True)
	vat = models.FloatField(default=0, null=True)
	created_date = models.DateField(auto_now_add=True, null=True)
	modified_date = models.DateField(auto_now= True)
    	

class products(models.Model):
	invoice = models.ForeignKey(invoice, on_delete=models.CASCADE)
	description = models.CharField(max_length=200, default=None, null=True)
	unit_price = models.FloatField(default=0, null=True)
	quantity = models.FloatField(default=0, null=True)
	vat_rate = models.FloatField(default=0, null=True)

class payment_status(models.Model):
	invoice = models.ForeignKey(invoice, on_delete=models.CASCADE)
	status = models.CharField(max_length = 255, default=None, null=True)