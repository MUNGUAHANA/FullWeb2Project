# Generated by Django 3.2.13 on 2024-05-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Les_produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('Details', models.TextField(blank=True)),
                ('Quantity', models.IntegerField(default=0)),
                ('Unit_Price', models.IntegerField(default=0)),
                ('Total_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='se_connecter',
            fields=[
                ('password', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('User_name', models.CharField(max_length=100, unique=True)),
                ('Adress_of_the_User', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('quantityBuy', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
                ('confirm', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.les_produits', to_field='name')),
            ],
        ),
    ]
