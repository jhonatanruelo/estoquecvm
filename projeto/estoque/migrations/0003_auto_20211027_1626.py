# Generated by Django 2.2.24 on 2021-10-27 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20211027_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='estoque_produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='NOME_DO_PRODUTO', to='produto.Produto'),
        ),
    ]