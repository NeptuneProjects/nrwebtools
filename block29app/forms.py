from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML
from django.urls import reverse_lazy

from .models import Block29


class Block29Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Block29Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Primary Duty',
                'pri_long',
                'pri_len',
                'pri_desc'
            ),
            HTML('<hr/>'),
            Fieldset(
                'Collateral Duty (optional)',
                'coll_long',
                'coll_len',
                'coll_desc'
            ),
            HTML('<hr/>'),
            Fieldset(
                'Watch (optional)',
                'watch',
                'watch_len',
            ),
            HTML('<hr/>'),
            Fieldset(
                'Mobilization',
                'umuic',
                'cross',
                'mob'
            ),
            HTML('<hr/>'),
            Fieldset(
                'PFA (optional)',
                'pfa'
            ),
            HTML('<hr/>'),
            Fieldset(
                'AT/ADT (optional)',
                'atadt1',
                'atadt2'
            ),
            HTML('<hr/>')
        )
        self.helper.form_action = reverse_lazy("/block29app/")
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.form_method = "POST"
    
    class Meta:
        model = Block29
        fields = '__all__'
        widgets = {
            'pri_long': forms.TextInput(attrs={'name': 'Title', 'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'pri_len': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'pri_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', 'style': 'margin: 0rem auto 1rem auto'}),
            'coll_long': forms.TextInput(attrs={'name': 'Title', 'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'coll_len': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'coll_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', 'style': 'margin: 0rem auto 1rem auto'}),
            'watch': forms.TextInput(attrs={'name': 'Title', 'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'watch_len': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'umuic': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'mob': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto'}),
            'pfa': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto', 'placeholder': 'E.g., CY22, 19-1/19-2'}),
            'atadt1': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto', 'placeholder':'E.g., 22Jul10-22Jul24, RIMPAC, COMPACFLT, Pearl Harbor, HI'}),
            'atadt2': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin: 0rem auto 1rem auto', 'placeholder':'E.g., 22Jul10-22Jul24, RIMPAC, COMPACFLT, Pearl Harbor, HI'})
        }
        labels = {
            'pri_long': 'Title',
            'pri_len': 'Duration (months)',
            'pri_desc': 'Description',
            'coll_long': 'Title',
            'coll_len': 'Duration (months)',
            'coll_desc': 'Description',
            'watch': 'Watch',
            'watch_len': 'Duration (months)',
            'umuic': 'UMUIC',
            'cross': 'Cross assigned',
            'mob': 'Mobilization Billet',
            'pfa': 'Which PFA scores are being reported?',
            'atadt1': 'AT/ADT Support 1',
            'atadt2': 'AT/ADT Support 2'
        }
