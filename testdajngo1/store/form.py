from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    slug= forms.SlugField(required=True)
    authr= forms.CharField(required=True, widget=forms.Textarea( attrs={"placeholder": "authr name"}))
    price = forms.FloatField(min_value=1.00)
    description= forms.TimeField(required=True, widget=forms.Textarea(
                                                                attrs={
                                                                    "class": "new-class-name",
                                                                    "id": "my_id_description",
                                                                    "rows": 10,
                                                                    "columns": 4
                                                                }
                                                            ))
    class Meta:
        model= Product
        fields=[
           'slug',
           'authr',
           'description',
           'price']


    def clean_slug(self, *args, **kwargs):  #validatio function slug input
        slug =self.cleaned_data.get("slug")
        if slug == "not slug":
            raise forms.ValidationError(" This is not a valid slug") # this will be printed in html
        return slug



class RawProductForm(forms.Form):
    slug= forms.SlugField(required=True)
    authr= forms.CharField(required=True)
    price = forms.FloatField(min_value=1.00)
    description= forms.TimeField(required=True, widget=forms.Textarea(

                                                                attrs={
                                                                    "class": "new-class-name",
                                                                    "id": "my_id_description",
                                                                    "rows": 10,
                                                                    "columns": 4
                                                                }
                                                            ))
