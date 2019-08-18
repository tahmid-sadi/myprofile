from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    blogimage = models.ImageField(upload_to='Blogimages/')


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:40]


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
