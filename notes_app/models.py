from django.db import models

# Create your models here.


class Post(models.Model):
    """
    Model representing a bulletin board post.
    Fields:
    - title: CharField for the post title with a maximum length of 50
    characters.
    - description: TextField for the post content.
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    created_by = models.CharField(max_length=50)
