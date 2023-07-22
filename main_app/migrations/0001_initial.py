# Generated by Django 3.2.15 on 2023-07-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='about/')),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='blog_image/')),
                ('short_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardsUnderSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider/')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FooterContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/')),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('footer_text', models.TextField(blank=True, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/')),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('blog_text', models.TextField(blank=True, null=True)),
                ('footer_text', models.TextField(blank=True, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='package_image/')),
                ('hotel_status', models.TextField(blank=True, null=True)),
                ('hotel_distance', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_page', models.ImageField(blank=True, null=True, upload_to='page/')),
                ('contact', models.ImageField(blank=True, null=True, upload_to='page/')),
                ('all_package', models.ImageField(blank=True, null=True, upload_to='page/')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider/')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='PackageImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='package_image/')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.package')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='order_files/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.package')),
            ],
        ),
        migrations.CreateModel(
            name='DiseasesExplanation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deseases', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.diseases')),
            ],
        ),
    ]