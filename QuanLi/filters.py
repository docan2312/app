import django_filters
from django_filters import CharFilter

from .models import *

class Detail_CongDoanVienFilter(django_filters.FilterSet):
    class Meta:
        model = CongDoanVien
        fields = ('MaCDV', 'HoTen', 'NgaySinh', 'NgayVaoNganh',)

class CongDoanVienFilter(django_filters.FilterSet):
    MaDonVi = CharFilter(field_name='MaDonVi', lookup_expr='icontains')
    TenDonVi = CharFilter(field_name='TenDonVi', lookup_expr='icontains')
    class Meta:
        model = CongDoanVien
        fields = '__all__'

class TourFilter(django_filters.FilterSet):
    MaTour = CharFilter(field_name='MaTour', lookup_expr='icontains')
    DiaDiem = CharFilter(field_name='DiaDiem', lookup_expr='icontains')
    class Meta:
        model = Tour
        fields = '__all__'

