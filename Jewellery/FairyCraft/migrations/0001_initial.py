# Generated by Django 5.2.3 on 2025-06-29 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jewellery_Type',
            fields=[
                ('ID_jewType', models.AutoField(primary_key=True, serialize=False)),
                ('jew_name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Metall',
            fields=[
                ('ID_metallType', models.AutoField(primary_key=True, serialize=False)),
                ('metall_name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('ID_role', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField()),
                ('role_desc', models.CharField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('ID_status', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField()),
                ('status_desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jewellery',
            fields=[
                ('ID_jewellery', models.AutoField(primary_key=True, serialize=False)),
                ('jewellery_name', models.CharField()),
                ('jewellery_desc', models.CharField()),
                ('jewellery_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creationDate', models.DateField(help_text='Введите дату в формате ГГГГ-ММ-ДД')),
                ('jewellery_img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('jewType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.jewellery_type')),
                ('metalType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.metall')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID_user', models.AutoField(primary_key=True, serialize=False)),
                ('mail_address', models.EmailField(max_length=254, unique=True)),
                ('us_password', models.CharField()),
                ('us_surname', models.CharField()),
                ('us_name', models.CharField()),
                ('phone_num', models.CharField()),
                ('in_job', models.IntegerField(blank=True, null=True)),
                ('us_img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.role')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ID_order', models.AutoField(primary_key=True, serialize=False)),
                ('dateOfPrepare', models.DateField(help_text='Введите дату в формате ГГГГ-ММ-ДД')),
                ('jewellery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.jewellery')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.status')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.user')),
            ],
        ),
        migrations.AddField(
            model_name='jewellery',
            name='jew_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FairyCraft.user'),
        ),
    ]
