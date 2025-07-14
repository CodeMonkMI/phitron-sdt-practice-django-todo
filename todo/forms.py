from django import forms
from todo.models import Todo


class TodoCreateFrom(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            "text",
            "description",
        ]
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-200 outline-none px-3 py-2 rounded"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full border border-gray-200 px-3 py-2 rounded outline-none",
                    "rows": "2",
                }
            ),
        }
