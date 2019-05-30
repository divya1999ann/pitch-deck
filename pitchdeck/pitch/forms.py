from django import forms
from django.contrib.auth.models import User
from pitch.models import userprofile,startup_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')


class userprofileform(forms.ModelForm):
    class Meta:
        model=userprofile
        fields=('website','picture')

class startup_Form(forms.ModelForm):
    class Meta:
        model=startup_data
        fields='__all__'

class u_nameform(forms.ModelForm):
    class Meta:
        model=u_name
        fields=('companyname','company_slogan','problem_head','problem_description','solution_head','solution_description','TAM','SAM','CMS','product_name','product_description',
                'IPAcquistion','potential_market','partnership','exist_sales','market_program','CAV_CAC','competitor1','competitor2',
                'fund_expect','fund_raised','competitor3','different','name1','desig1','name2','desig2','name3','desig3','fund_need',
                'fund_return','email','phone','address','link_linkedin','link_facebook','link_twitter' )











