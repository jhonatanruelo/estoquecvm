# Generated by Django 2.2.24 on 2021-10-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='estoque_produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='NOME_DO_PRODUTO', to='produto.Produto'),
            preserve_default=False,
        ),
    ]
