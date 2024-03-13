from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["title"].widget.attrs["placeholder"] = "Title"
        self.fields["title"].label = ""
        
        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs["placeholder"] = "Description"
        self.fields["description"].label = ""
        
