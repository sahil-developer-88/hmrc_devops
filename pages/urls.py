from django.urls import path, include
from . import views, views_agent, views_sa
from .views import displayall,MtdView, FileListView, AgentView,FileEditView, UploadFileView, HomeView, TestView, InitView, TuView, MtdView, FileEditView, VatLiabilitiesView, VatPaymentView, VatObligationsView, VatReturnView, InvoiceListView , InvoiceView, InvoiceDetailsView, InvoiceCreateView
from .views_agent import    a_testagent
from .pm import pm1, pm3,about, delete, cross_off,cross_on,edit,about2, delete2, cross_off2,cross_on2,edit2 

#app_name = 'mtd'

urlpatterns = [
    # path('mtd', views.MtdView.as_view(), name="mtd"),
    path('', views.MtdView.as_view(), name="mtd"),
    path('init/', views.InitView.as_view(), name="init"),


    path('displayall/', views.displayall.as_view(), name="displayall"),

    path('testuser/', views.TuView.as_view(), name="tuview"),
    path('mtd2/', views.MtdView2.as_view(), name="mtdview"),

    path('agentservices/', views.AgentView.as_view(), name="mtdview"),
    path('clientview/', views.ClientView.as_view(), name="clientview"),

    path('file-edit/', FileEditView.as_view(), name='file_edit'),
    #createagent 
    path('a_testagent/', views_agent.a_testagent.as_view(), name="tuview_agent"),
    #callback of createagent 
    path('mtd2agent/', views_agent.MtdView2.as_view(), name="mtdviewagent"), #seprate testuser and testagent due to vrn /arn json decomp names 

    path('a_last30/', views_agent.a_last30.as_view(), name="a_last30"),
    path('a_new_auth/', views_agent.a_new_auth.as_view(), name="a_new_auth"),
    path('a_get_invite/', views_agent.a_get_invite.as_view(), name="a_get_invite"),
    path('a_get_relationship/', views_agent.a_get_relationship.as_view(), name="a_get_relationship"),
    path('a_cancel_invite/', views_agent.a_cancel_invite.as_view(), name="a_cancel_invite"),
    path('refresh_token/', views_agent.refresh_token.as_view(), name="refresh_token"),

    path('saservices/', views.AgentView_sa.as_view(), name="AgentView_sa"),
    path('sa_testuser/', views_sa.sa_testuser.as_view(), name="sa_testuser"),


    # sub navigations
    path('vat-liabilities/', VatLiabilitiesView.as_view(), name = "vat-liabilities"),
    path('vat-payment/', VatPaymentView.as_view(), name = "vat-payment"),
    path('vat-obligations/', VatObligationsView.as_view(), name = "vat-obligations"),
    path('vat-return/', VatReturnView.as_view(), name = "vat-return"),

    path('pm/',pm1.as_view(), name="pm"),
    path('pm2/',pm3.as_view(), name="pm2"), #make sure in pm.py class name is diff from model name, p1 class, pm model, pm3 class, p2 model etc etc
    
    path ('about/',about.as_view(), name='about'),
    path ('delete/<list_id>',delete.as_view(), name='delete'),
    path ('cross_off/<list_id>',cross_off.as_view(), name='cross_off'),
    path ('cross_on/<list_id>',cross_on.as_view(), name='cross_on'),
    path ('edit/<list_id>',edit.as_view(), name='edit'),

    path ('about2/',about2.as_view(), name='about2'),
    path ('delete2/<list_id>',delete2.as_view(), name='delete2'),
    path ('cross_off2/<list_id>',cross_off2.as_view(), name='cross_off2'),
    path ('cross_on2/<list_id>',cross_on2.as_view(), name='cross_on2'),
    path ('edit2/<list_id>',edit2.as_view(), name='edit2'),


    path('invoice/create/',InvoiceView.as_view(), name="invoice-create"),
    path('invoice/<int:id>/',InvoiceView.as_view(), name="invoice"),
    
    path('invoice-list/',InvoiceListView.as_view(), name="invoice-list"),
    path('invoice-details/<int:id>/',InvoiceDetailsView.as_view(), name="invoice-details"),        
	# path ('mtd2/',views.mtd_home2.as_view(), name='mtd_home2'),
]