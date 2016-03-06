# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street', models.CharField(max_length=50)),
                ('PostalZipCode', models.CharField(max_length=15)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=254)),
                ('FullName', models.CharField(max_length=150)),
                ('Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Authentication_Address', to='main.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Modes', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Address')),
            ],
        ),
        migrations.CreateModel(
            name='CarrierCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=15)),
                ('Type', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Carrier')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('StateRegionName', models.CharField(max_length=120)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Client_Address', to='main.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ClientCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=100)),
                ('CodeType', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ClientSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=120)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Address')),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Mobile', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Address')),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ContainerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('Container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Container')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('ISO_3_Code', models.CharField(max_length=3)),
                ('ISO_2_Code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrencyName', models.CharField(max_length=120)),
                ('CurrencyCode', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Unit', models.CharField(max_length=50)),
                ('Weight', models.IntegerField()),
                ('WeightType', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sequence', models.IntegerField()),
                ('ScheduledDate', models.DateTimeField()),
                ('ActualDate', models.DateTimeField()),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.City')),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
                ('Contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='EventGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Sequence', models.IntegerField()),
                ('BillNumber', models.CharField(max_length=12)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Carrier')),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=50)),
                ('Amount', models.FloatField()),
                ('EffectiveDate', models.DateField()),
                ('ExpirationDate', models.DateField()),
                ('Currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Seal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Container')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SecurityType', models.CharField(max_length=50)),
                ('BillNumberPrefix', models.CharField(max_length=4)),
                ('ParentBillNumberPrefix', models.CharField(max_length=4)),
                ('OriginalSentDate', models.DateTimeField()),
                ('OriginalAcceptedDate', models.DateTimeField()),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillNumber', models.CharField(max_length=12)),
                ('ShipperName', models.CharField(max_length=120)),
                ('ConsigneeName', models.CharField(max_length=120)),
                ('NotifyName', models.CharField(max_length=120)),
                ('Notify2Name', models.CharField(max_length=120)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
                ('Consigee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Consigee', to='main.Address')),
                ('Notify', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notify', to='main.Address')),
                ('Notify2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notify2', to='main.Address')),
                ('Shipper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Shipper', to='main.Address')),
            ],
        ),
        migrations.CreateModel(
            name='StockKeepingUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('Weight', models.IntegerField()),
                ('WeightType', models.CharField(max_length=50)),
                ('HarmonizedTariffCode', models.CharField(max_length=50)),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Description', models.CharField(max_length=50)),
                ('Amount', models.FloatField()),
                ('CreatedByUser', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedByUser', models.CharField(max_length=50)),
                ('UpdatedDate', models.DateTimeField(auto_now=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
                ('Currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Currency')),
            ],
        ),
        migrations.AddField(
            model_name='security',
            name='Shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Shipment'),
        ),
        migrations.AddField(
            model_name='eventgroup',
            name='Shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Shipment'),
        ),
        migrations.AddField(
            model_name='event',
            name='EventGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.EventGroup'),
        ),
        migrations.AddField(
            model_name='event',
            name='Shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Shipment'),
        ),
        migrations.AddField(
            model_name='detail',
            name='StockKeepingUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.StockKeepingUnit'),
        ),
        migrations.AddField(
            model_name='containerdetail',
            name='Detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Detail'),
        ),
        migrations.AddField(
            model_name='container',
            name='Shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Shipment'),
        ),
        migrations.AddField(
            model_name='clientsubscription',
            name='Subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subscription'),
        ),
        migrations.AddField(
            model_name='city',
            name='Country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Country'),
        ),
        migrations.AddField(
            model_name='carriercode',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client'),
        ),
        migrations.AddField(
            model_name='authentication',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Authentication_Client', to='main.Client'),
        ),
        migrations.AddField(
            model_name='address',
            name='City',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City', to='main.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='UpdatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UpdatedByUser', to='main.Authentication'),
        ),
    ]