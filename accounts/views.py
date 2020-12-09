from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
# Create your views here.

def home(request):
    dosen = len(models.Dosen.objects.all())
    mhs = len(models.Mahasiswa.objects.all())
    matkul = len(models.Matakuliah.objects.all())

    return render(request,'home.html',{'dosen':dosen,'mhs':mhs,'matkul':matkul})

def dosen(request):
    dosen = models.Dosen.objects.all()
    return render(request,'dosen.html',{'dosen':dosen})

def tambahDosen(request):
    if request.method == "POST":
        dosen = request.POST["namaDosen"]
        if models.Dosen.objects.filter(nama=dosen).exists():
            messages.info(request, 'Nama Dosen Sudah Ada.')
            return redirect(tambahDosen)
        else:
            a = models.Dosen(nama=dosen)
            a.save()
            messages.info(request, 'Data Dosen Telah Ditambahkan.')
            return redirect(tambahDosen)

    else:
        return render(request,'tmbhdosen.html')

def ubahDosen(request,ids):
    dosens = models.Dosen.objects.filter(id=ids)
    if dosens:
        if request.method == "POST":
            dosens = models.Dosen.objects.get(id=ids)
            dosens.nama = request.POST['namaDosen']
            dosens.save()
            return redirect(dosen)
        else:
            return render(request,'ubahdosen.html',{'dosen':dosens.first})
    else:
        return redirect(dosen)

def delDosen(request):
    if request.method == 'POST':
        id = request.POST['idDosen']
        check = models.Matakuliah.objects.filter(id_dosen_id=id)
        if check:
            messages.info(request, 'Dosen Masih Terikat Dengan Matakuliah.')
            return redirect(dosen)
        else:
            dosens = models.Dosen.objects.get(id=id)
            dosens.delete()
            messages.info(request, 'Data Dosen Berhasil di Delete.')
            return redirect(dosen)
        return redirect(dosen)
    else:
        return redirect(dosen)



def mahasiswa(request):
    mhs = models.Mahasiswa.objects.all()
    return render(request,'mahasiswa.html',{'mhs':mhs})

def tambahMahasiswa(request):
    if request.method == "POST":
        mahasiswa = request.POST["namaMahasiswa"]
        nim = request.POST["nim"]
        prodi = request.POST["prodi"]
        fakultas = request.POST["fakultas"]
        if models.Mahasiswa.objects.filter(nama=mahasiswa).exists() or models.Mahasiswa.objects.filter(nim=nim).exists():
            messages.info(request, 'Nama/NIM mahasiswa Sudah Ada.')
            return redirect(tambahMahasiswa)
        else:
            a = models.Mahasiswa(nama=mahasiswa,nim=nim,prodi=prodi,fakultas=fakultas)
            a.save()
            messages.info(request, 'Data Mahasiswa Telah Ditambahkan.')
            return redirect(tambahMahasiswa)

    else:
        return render(request,'tmbhmahasiswa.html')
def ubahMahasiswa(request,ids):
    mhs = models.Mahasiswa.objects.filter(id=ids)
    if mhs:
        if request.method == "POST":
            mahasiswas = models.Mahasiswa.objects.get(id=ids)
            mahasiswas.nama = request.POST['namaMahasiswa']
            mahasiswas.nim = request.POST['nim']
            mahasiswas.prodi = request.POST['prodi']
            mahasiswas.fakultas = request.POST['fakultas']
            mahasiswas.save()
            return redirect(mahasiswa)
        else:
            return render(request,'ubahmahasiswa.html',{'mhs':mhs.first})
    else:
        return redirect(mahasiswa)
# delmahasiswa harus nunggu tabel nilai buat forignkey
def delMahasiswa(request):
    if request.method == 'POST':
        id = request.POST['idMhs']
        check = models.Raport.objects.filter(id_mahasiswa_id=id)
        if check:
            messages.info(request, 'Mahasiswa Masih Terikat Dengan Raport.')
            return redirect(mahasiswa)
        else:
            mahasiswas = models.Mahasiswa.objects.get(id=id)
            mahasiswas.delete()
            messages.info(request, 'Data Mahasiswa Berhasil di Delete.')
            return redirect(mahasiswa)
        return redirect(mahasiswa)
    else:
        return redirect(mahasiswa)






def matkul(request):
    matkul = models.Matakuliah.objects.all().select_related('id_dosen')
    return render(request,'matkul.html',{'matkul':matkul})

def tambahMatkul(request):
    if request.method == "POST":
        matkul = request.POST["matkul"]
        idDosen = request.POST["idDosen"]
        if models.Matakuliah.objects.filter(nama_matakuliah=matkul).exists():
            messages.info(request, 'Nama MataKuliah Sudah Ada.')
            return redirect(tambahMatkul)
        else:
            a = models.Matakuliah(nama_matakuliah=matkul,id_dosen_id=idDosen)
            a.save()
            messages.info(request, 'Data MataKuliah Telah Ditambahkan.')
            return redirect(tambahMatkul)
    else:
        lis_dosen = models.Dosen.objects.all()
        return render(request,'tmbhmatkul.html',{'lis_dosen':lis_dosen})
def ubahMatkul(request,ids):
    matakul = models.Matakuliah.objects.filter(id=ids)
    if matakul:
        if request.method == "POST":
            matkuls = models.Matakuliah.objects.get(id=ids)
            matkuls.nama_matakuliah = request.POST['matkul']
            matkuls.id_dosen_id = request.POST['idDosen']
            matkuls.save()
            return redirect(matkul)
        else:
            lis_dosen = models.Dosen.objects.all()
            return render(request,'ubahmatkul.html',{'matkul':matakul.first,'lis_dosen':lis_dosen})
    else:
        return redirect(matkul)
def delMatkul(request):
    if request.method == 'POST':
        id = request.POST['idMatkul']
        check = models.NilaiDetil.objects.filter(id_matkul_id=id)
        if check:
            messages.info(request, 'Matkul Masih Terikat Dengan Nilai.')
            return redirect(matkul)
        else:
            matkuls = models.Matakuliah.objects.get(id=id)
            matkuls.delete()
            messages.info(request, 'Data Matkul Berhasil di Delete.')
            return redirect(matkul)
        return redirect(matkul)
    else:
        return redirect(matkul)


def nilai(request):
    rapor = models.Raport.objects.all().select_related('id_mahasiswa')
    return render(request,'nilai.html',{'rapor':rapor})

def tambahNilai(request):
    matkul = models.Matakuliah.objects.all()
    if request.method == "POST":
        id = request.POST['idMhs']
        rapor = models.Raport(id_mahasiswa_id = id )
        rapor.save()
        for x in matkul:
            detail = models.NilaiDetil(nilai=request.POST[x.nama_matakuliah],id_matkul_id=x.id,id_raport_id=rapor.id)
            detail.save()
        messages.info(request, 'Data Raport Berhasil di tambahkan.')
        return redirect(nilai)
    else:
        raport = models.Raport.objects.all()
        mhs = models.Mahasiswa.objects.all()
        return render(request,'tmbhnilai.html',{'matkul':matkul,'raport':raport,'mhs':mhs})
def ubahNilai(request,ids):
    rapor = models.NilaiDetil.objects.filter(id_raport_id=ids).select_related('id_matkul')
    nama = models.Raport.objects.filter(id=ids).select_related('id_mahasiswa').first().id_mahasiswa
    if rapor:
        if request.method == "POST":
            for x in rapor:
                rapors = models.NilaiDetil.objects.get(id=x.id)
                rapors.nilai = request.POST[x.id_matkul.nama_matakuliah]
                rapors.id_matkul_id = x.id_matkul.id
                rapors.save()
            messages.info(request, 'Data Nilai Berhasil di Update.')
            return redirect(nilai)
        else:
            return render(request,'ubahnilai.html',{'rapor':rapor,'nama':nama})
    else:
        return redirect(nilai)

def viewNilai(request,ids):
    rapor = models.NilaiDetil.objects.filter(id_raport_id=ids).select_related('id_matkul')
    nama = models.Raport.objects.filter(id=ids).select_related('id_mahasiswa').first().id_mahasiswa
    return render(request,'viewnilai.html',{'rapor':rapor,'nama':nama}) 

def delNilai(request):
    if request.method == "POST":
        id = request.POST['idNilai']
        models.NilaiDetil.objects.filter(id_raport_id=id).delete()
        models.Raport.objects.get(id=id).delete()
        messages.info(request, 'Data Nilai Berhasil di Delete.')
        return redirect(nilai)
    else:
        return redirect(nilai)