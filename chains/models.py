from django.db import models

class Category(models.Model):
    """Food category (Burgers, Pizza, etc.)"""
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    """Chain attributes (Drive-Thru, Delivery, etc.)"""
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Chain(models.Model):
    """Fast food chain"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='chains')
    tags = models.ManyToManyField(Tag, related_name='chains', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']