# Generated by Django 4.2 on 2024-11-04 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_course_file_alter_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='file',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French')], default='English', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intemediate', 'Intemediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='platform_status',
            field=models.CharField(blank=True, choices=[('Review', 'Review'), ('Disabled', 'Disabled'), ('Rejected', 'Rejected'), ('Draft', 'Draft'), ('Published', 'Published')], default='Published', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.teacher'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
