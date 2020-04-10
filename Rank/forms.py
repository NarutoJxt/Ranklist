
from django import forms
from Rank.models import User


class RankInsertionForm(forms.ModelForm):
    CLIENT_CHOICE = [
        (i,i) for i in range(1,10000)
    ]

    client = forms.IntegerField(
        widget=forms.Select(choices=CLIENT_CHOICE,
            attrs={
                "class":"form-control"
            }
                            )
        ,
    )
    score = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"请输入分数(1-10000000)","class":"form-control"
            }
        ),
        required = True
    )
    class Meta:
        model = User
        fields = ["client","score"]