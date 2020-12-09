from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    prodi = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)

class Dosen(models.Model):
    nama = models.CharField(max_length=50)

class Matakuliah(models.Model):
    nama_matakuliah = models.CharField(max_length=50)
    id_dosen = models.ForeignKey(Dosen, on_delete=models.RESTRICT)

class Raport(models.Model):
    id_mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.RESTRICT)

class NilaiDetil(models.Model):
    id_raport = models.ForeignKey(Raport, on_delete=models.CASCADE)
    id_matkul = models.ForeignKey(Matakuliah, on_delete=models.RESTRICT)
    nilai = models.IntegerField()
    

