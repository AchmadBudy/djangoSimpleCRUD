# Generated by Django 3.1.4 on 2020-12-04 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('prodi', models.CharField(max_length=50)),
                ('fakultas', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matakuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_matakuliah', models.CharField(max_length=50)),
                ('id_dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dosen')),
            ],
        ),
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.IntegerField()),
                ('id_mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.mahasiswa')),
                ('id_matakuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.matakuliah')),
            ],
        ),
    ]
