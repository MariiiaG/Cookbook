from .models import Recipe, Category
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = (UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email'))


class NewTemplate(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_method', 'cooking_time', 'image']


    # class Meta:
    #     model = Recipe
    #     fields = '__all__'
    #     widgets = {
    #         'owner': forms.HiddenInput
    #     }



    # category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    # class Meta:
    #     model = Recipe
    #     fields = ['title', 'description', 'cooking_method', 'cooking_time', 'image']
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control'}),
    #         'description': forms.Textarea(attrs={'class': 'form-control'}),
    #         'cooking_method': forms.Textarea(attrs={'class': 'form-control'}),
    #         'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'image': forms.FileInput(attrs={'class': 'form-control'}),
    #    }


class NewCatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class LoginForm(AuthenticationForm):
    pass
