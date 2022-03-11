from django import forms
from .models import Course



class KursRegisterForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Введите URL адрес вашего будущего курса',
        help_text="Вводите собственно придуманный Url.",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        label='Введите название вашего будущего курса',
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label='Введите текст вашего будущего курса',
        max_length=500,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    img = forms.ImageField(
        label='Вставьте картинку для вашего будущего курса',
        required=False,
        help_text="( необязательно )"
    )

    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']
