from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dosen', views.dosen),
    path('dosen/tambah', views.tambahDosen),
    path('dosen/<int:ids>', views.ubahDosen),
    path('dosen/delete', views.delDosen),
    path('mahasiswa', views.mahasiswa),
    path('mahasiswa/<int:ids>', views.ubahMahasiswa),
    path('mahasiswa/tambah', views.tambahMahasiswa),
    path('mahasiswa/delete', views.delMahasiswa),
    path('matkul', views.matkul),
    path('matkul/tambah', views.tambahMatkul),
    path('matkul/delete', views.delMatkul),
    path('matkul/<int:ids>', views.ubahMatkul),
    path('nilai', views.nilai),
    path('nilai/tambah', views.tambahNilai),
    path('nilai/<int:ids>', views.ubahNilai),
    path('nilai/<int:ids>/view', views.viewNilai),
    path('nilai/delete', views.delNilai),
]