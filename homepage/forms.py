from django import forms

from .models import Post


class HomeForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()
    income = forms.IntegerField()
    years = forms.IntegerField()

    class Meta:
        model = Post
        fields = ('name', 'age', 'income', 'years', )


class BMIForm(forms.ModelForm):
    name = forms.CharField()
    weight = forms.IntegerField()
    feet = forms.IntegerField()
    inches = forms.IntegerField()

    class Meta:
        model = Post
        fields = ('name', 'weight', 'feet', 'inches',)