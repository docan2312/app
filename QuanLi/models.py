from django.db import models
from django import forms
class DonVi(models.Model):
    MaDonVi = models.CharField(max_length=5, blank=True)
    TenDonVi = models.CharField(max_length=50)
    def __str__(self):
        return self.TenDonVi
    def __unicode__(self):
        return self.MaDonVi
class Tour(models.Model):
    MaTour = models.CharField(max_length=5, blank=True)
    DiaDiem = models.CharField(max_length=1000)
    NgayDi = models.DateField()
    NgayVe = models.DateField()
    ChiTiet = models.TextField(null=True)
    def __str__(self):
        return self.DiaDiem
    def __unicode__(self):
        return self.MaTour

class CongDoanVien(models.Model):
    DonVi = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    MaCDV = models.CharField(max_length=5, blank=True)
    HoTen = models.CharField(max_length=100, blank=True)
    NgaySinh = models.DateField()
    NgayVaoNganh = models.DateField()
    def __str__(self):
        return self.HoTen
    def __unicode__(self):
        return self.MaCDV

class DKTour(models.Model):
    CongDoanVien = models.ForeignKey(CongDoanVien, on_delete=models.CASCADE)
    Tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

class TaiKhoan(models.Model):
    MaCDV = models.OneToOneField(CongDoanVien, on_delete=models.CASCADE, primary_key=True)
    MatKhau = models.CharField(max_length=10)

