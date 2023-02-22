from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

STATUS_TYPES = (
    ('new', 'Новая задача'),
    ('in order', 'В процессе'),
    ('finishde', 'Завершено')
)


class TaskForm(forms.Form):
    description = forms.CharField(max_length=20, required=True, label='Заголовок')
    status = forms.ChoiceField(required=True, label='Статус', choices=STATUS_TYPES)
    finish_date = forms.DateField(required=True, label='Дата выполнения (Год-Месяц-День)')
    detail_description = forms.CharField(max_length=1000, required=True, label='Описание', widget=widgets.Textarea)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 3:
            raise ValidationError('Заголовок должен быть длиннее 3 символов')
        return description

    def clean_detail_description(self):
        detail_description = self.cleaned_data.get('detail_description')
        if len(detail_description) < 5:
            raise ValidationError('Описание должно быть длиннее 5 символов')
        return detail_description
