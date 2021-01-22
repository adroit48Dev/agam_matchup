from django.db import models

# class FileField([upload_to=None, max_length=100, **options])



# Create your models here.
class Templates(models.Model):
    # templ_id = models.IntegerField(primary_key=True)
    temp_name = models.CharField(max_length=100)


class Matchup(models.Model):
    template_name = models.ForeignKey(Templates, related_name='lists', null=True, on_delete=models.SET_NULL)
    matchup_id = models.AutoField(primary_key=True, unique=True)
    image = models.FileField(max_length=200, upload_to="media/", blank=True, null=True)
    keyword = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
            return self.template_name
