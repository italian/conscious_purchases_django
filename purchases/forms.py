from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'user',
            'item',
            'last_purchase_date',
            'time_since_last_purchase',
            'result',
            ]


class ChecklistForm(forms.Form):
    need_this = forms.ChoiceField(
        choices=[('да', 'Да'), ('нет', 'Нет')],
        label='Нужно ли вам это?')
    need_this_seriously = forms.ChoiceField(
        choices=[('да', 'Да'), ('нет', 'Нет')],
        label='Серьезно?')
    need_this_yesterday = forms.ChoiceField(
        choices=[('да', 'Да'), ('нет', 'Нет')],
        label='Вам было нужно это вчера?')
    can_borrow_or_rent = forms.ChoiceField(
        choices=[('да', 'Да'), ('нет', 'Нет')],
        label='Можете ли в это одолжить или арендовать?')
    want_to_keep = forms.ChoiceField(
        choices=[('да', 'Да'), ('нет', 'Нет')],
        label='Вы хотите это хранить?')
