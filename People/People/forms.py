from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(required=True)
