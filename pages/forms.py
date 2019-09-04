from django import forms
from .models import pm

class ListForm( forms.ModelForm):
	class Meta:
		model=pm
		fields = ['sprint', 'asignee', 'status','epic','priority','estimation','status2','status3','status4','status5','src_sys_id']