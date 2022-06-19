from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighborhood')
    logo = CloudinaryField('image',null=True, blank=True)
    health_number = models.IntegerField(null=True)
    police_number = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
       ordering = ['-date']


    def __str__(self):
        return f'{self.name} neighbhood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def all_neighborhoods(cls):
        return cls.objects.all()    

    @classmethod
    def search_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = CloudinaryField('image',null=True, default='default.png')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='ocupants', blank=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    price = models.IntegerField(null=True)


    class Meta:
       ordering = ['-date']

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_owner')
    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighborhood_post')



