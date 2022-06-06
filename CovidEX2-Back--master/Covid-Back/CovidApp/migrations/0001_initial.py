from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.PositiveIntegerField(null=True)),
                ('landline', models.CharField(max_length=100)),
                ('cellular_phone', models.CharField(max_length=100)),
                ('is_covid_19_infected', models.BooleanField()),
                ('have_diabetes', models.BooleanField()),
                ('have_cardio_problems', models.BooleanField()),
                ('have_allergies', models.BooleanField()),
                ('have_other_medical_conditions', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
