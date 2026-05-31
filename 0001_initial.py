from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id',        models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('cnic',      models.CharField(max_length=20)),
                ('email',     models.EmailField(max_length=254)),
                ('phone',     models.CharField(max_length=20)),
                ('disease',   models.TextField()),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('doctor',    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='doctors.doctor')),
            ],
            options={'ordering': ['-booked_at']},
        ),
    ]
