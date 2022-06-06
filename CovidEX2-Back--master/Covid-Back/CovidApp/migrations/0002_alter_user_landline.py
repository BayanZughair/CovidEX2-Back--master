from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CovidApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='landline',
            field=models.CharField(max_length=50),
        ),
    ]
