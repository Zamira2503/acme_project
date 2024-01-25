# birthday/forms.py
from django import forms

MAX_LENGTH = 20

class BirthdayForm(forms.Form):
    first_name = forms.CharField(max_length=MAX_LENGTH)
    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'})
    ) 