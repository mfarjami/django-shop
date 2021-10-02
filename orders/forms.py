from django import forms

class CouponFrom(forms.Form):
    code = forms.CharField()