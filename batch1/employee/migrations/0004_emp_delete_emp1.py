# Generated by Django 4.0.2 on 2022-07-23 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20220623_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('department', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.reg')),
            ],
        ),
        migrations.DeleteModel(
            name='Emp1',
        ),
    ]