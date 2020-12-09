# Generated by Django 3.1.4 on 2020-12-07 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NilaiDetil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Raport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.mahasiswa')),
            ],
        ),
        migrations.AlterField(
            model_name='matakuliah',
            name='id_dosen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.dosen'),
        ),
        migrations.DeleteModel(
            name='Nilai',
        ),
        migrations.AddField(
            model_name='nilaidetil',
            name='id_matkul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.matakuliah'),
        ),
        migrations.AddField(
            model_name='nilaidetil',
            name='id_raport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.raport'),
        ),
    ]
