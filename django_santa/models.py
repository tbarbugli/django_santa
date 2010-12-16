from django.db import models

class Present(models.Model):
    description = models.CharField(max_length=100)
    karma_needed = models.IntegerField()

    def __unicode__(self):
        return self.description

class Child(models.Model):
    """
    >>> tommaso = Child.objects.create(name="tommaso", karma=100)
    >>> bazooka = Present.objects.create(description="Bazooka", karma_needed=100)
    >>> charcoal = Present.objects.create(description="Charcoal", karma_needed=0)       
    >>> wish = Wish.objects.create(present= bazooka, child= tommaso)      
    >>> [tommaso.wish_set.all().count()]
    [1]
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    karma = models.IntegerField()
    whished_presents = models.ManyToManyField(Present, through='Wish')
    
    def __unicode__(self):
        return self.name   
        
class Wish(models.Model):
    present = models.ForeignKey(Present)
    child = models.ForeignKey(Child)
    
    def __unicode__(self):
        return "%s wishes a %s" % (self.child, self.present)