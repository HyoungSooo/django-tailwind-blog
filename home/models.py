from django.db import models

# Create your models here.


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    content = models.TextField()
    thumbnail_img = models.ImageField(
        null=True, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class PuzzleCategory(models.Model):
    category = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.category


class Puzzle(models.Model):
    catgory = models.ForeignKey(
        PuzzleCategory, on_delete=models.CASCADE)
    problem = models.TextField()
    solution = models.TextField(blank=True, null=True)
    time = models.DateField(auto_now_add=True)
