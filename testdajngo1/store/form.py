from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields=[
           'slug',
           'authr',
           'description',
           'price']


class RawProductForm(forms.form):
    slug= forms.SlugField(required=True)
    authr= forms.CharField(required=True)
    price = forms.FloatField(min_value=1.00)
    description= forms.TimeField(required=True, widget=forms.Textarea(

                                                                attres={
                                                                    "class": "new-class-name",
                                                                    "id": "my_id_description",
                                                                    "rows": 10,
                                                                    "columns": 4
                                                                }
                                                            ))
