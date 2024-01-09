# Generated by Django 3.2.6 on 2024-01-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=10)),
                ('email', models.ManyToManyField(to='newsletters.NewsletterUser')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.DeleteModel(
            name='Newslatter',
        ),
    ]
