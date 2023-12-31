# Generated by Django 4.2.6 on 2023-12-08 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Increment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('DEPT_NO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=100)),
                ('LOC', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GRADE', models.IntegerField()),
                ('LOSAL', models.IntegerField()),
                ('HISAL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMPNO', models.IntegerField()),
                ('ENAME', models.CharField(max_length=100)),
                ('JOB', models.CharField(max_length=100)),
                ('MGR', models.IntegerField()),
                ('HIREDATE', models.DateField()),
                ('SAL', models.IntegerField()),
                ('COMM', models.IntegerField()),
                ('DEPT_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
