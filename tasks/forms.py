from django import forms 
from .models import Task, TaskPhoto

class TaskForm(forms.ModelForm):
    #photos = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Task
        fields= ['title', 'description','due_date','priority','complete']
        
        
class TaskPhotoForm(forms.ModelForm):
    class Meta:
        model = TaskPhoto
        fields = ['photo']