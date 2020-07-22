from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    bio = models.TextField(max_length=1400, default="hello")
    picture = models.ImageField(blank=True, null=True, upload_to="profile")
    slug = models.SlugField(blank=True, null=False ,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class History(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    amount=models.IntegerField(blank=False,null=False)

class Request(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title=models.CharField( max_length=100)
    content=models.TextField()
    pin=models.BooleanField(default=False)
    img=models.ImageField(upload_to="request",blank=False,null=False)
    created=models.TimeField( auto_now_add=True)
    inter=models.ForeignKey("Interact", on_delete=models.CASCADE,blank=True,null=True)
    total_vote=models.IntegerField(default=1)
    votes_total = models.ManyToManyField( settings.AUTH_USER_MODEL, related_name="votes" ,)
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Interact(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
    reque=models.ForeignKey(Request, on_delete=models.CASCADE,blank=True,null=True) 
    upvote=models.BooleanField(default=False)
    comment=models.CharField( max_length=140)
'''
    def save(self, *args, **kwargs):
        if self.user and Interact.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            return False
        
        return super(Interact, self).save(*args, **kwargs)
'''
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)