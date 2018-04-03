from django.db import models

class Tab(models.Model):
    n_projet = models.CharField(max_length=128)
    ref_projet = models.CharField(max_length=128)
    projet_ag = models.CharField(max_length=128)
    bui_temp = models.CharField(max_length=128)
    env = models.CharField(max_length=128)
    dt = models.CharField(max_length=128)
   
 #def __unicode__(self):
      #  return self.n_projet
def __str__(self):
    return self.n_projet


