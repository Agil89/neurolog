from django.db import models


# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.title}'

class CardsUnderSlider(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.title}'


class Diseases(models.Model):
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField()


class DiseasesExplanation(models.Model):
    name = models.CharField(max_length=255)
    deseases = models.ForeignKey(Diseases, on_delete=models.SET_NULL, null=True, blank=True)


class Package(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='package_image/', null=True, blank=True)
    hotel_status = models.TextField(null=True, blank=True)
    hotel_distance = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.title}'


class PackageImages(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='package_image/')


class Orders(models.Model):
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    message = models.TextField()
    file = models.FileField(upload_to='order_files/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} / {self.created_date}'





class Advantages(models.Model):
    number = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.title}'


class PageImages(models.Model):
    detail_page = models.ImageField(upload_to='page/', null=True, blank=True)
    contact = models.ImageField(upload_to='page/', null=True, blank=True)
    all_package = models.ImageField(upload_to='page/', null=True, blank=True)


class MainDatas(models.Model):
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    number = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    blog_text = models.TextField(null=True,blank=True)
    footer_text = models.TextField(null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    youtube_url = models.CharField(max_length=255,null=True,blank=True)
    linkedin_url = models.CharField(max_length=255,null=True,blank=True)



class ContactModel(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} / {self.created_date}'

class FooterContact(models.Model):
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    number = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    footer_text = models.TextField(null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    youtube_url = models.CharField(max_length=255,null=True,blank=True)
    linkedin_url = models.CharField(max_length=255,null=True,blank=True)

    
class Blogs(models.Model):
    title = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='blog_image/')
    short_desc = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    youtube_url = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about/')
    desc = models.TextField(null=True,blank=True)

    