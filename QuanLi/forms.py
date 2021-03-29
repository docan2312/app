from .models import CongDoanVien, Tour, DonVi, TaiKhoan, DKTour
from django import forms

from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm

#tao form them sua xoa cong doan
class Post_CongDoan (forms.ModelForm):
    class Meta:
        model = CongDoanVien
        fields = ('MaCDV', 'HoTen', 'NgaySinh', 'NgayVaoNganh', 'DonVi',)

    def clean_MaCDV(self):
        MaCDV = self.cleaned_data.get('MaCDV')
        for item in CongDoanVien.objects.all():
            if item.MaCDV == MaCDV:
                raise forms.ValidationError("Mã Công Đoàn Viên không được trùng" + MaCDV)
        return MaCDV

class CongDoan_Post (forms.ModelForm):
    class Meta:
        model = CongDoanVien
        fields = '__all__'

#tao form them sua xoa tour
class Post_Tour (forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'

    def clean_MaTour(self):
        MaTour = self.cleaned_data.get('MaTour')
        for item in Tour.objects.all():
            if item.MaTour == MaTour:
                raise forms.ValidationError('Mã Công Đoàn Viên không được trùng' + MaTour)
        return MaTour


class Tour_Post(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'
#tao form them sua xoa don vi
class Post_DonVi (forms.ModelForm):
    class Meta:
        model = DonVi
        fields = ('MaDonVi', 'TenDonVi',)

    def clean_MaDonVi(self):
        MaDonVi = self.cleaned_data.get('MaDonVi')
        for item in DonVi.objects.all():
            if item.MaDonVi == MaDonVi:
                raise forms.ValidationError('Mã Đơn Vị không được trùng' + MaDonVi)
        return MaDonVi

class DV_Post(forms.ModelForm):
    class Meta:
        model = DonVi
        fields = '__all__'

#################################
class Post_Login(forms.ModelForm):
    class Meta:
        model = TaiKhoan
        fields = '__all__'

class Post_DK(forms.ModelForm):
    class Meta:
        model = DKTour
        fields = '__all__'

#create UserForm
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
