from django.db import models


class BaseInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'name'):
            verbose_name = self.name
        elif hasattr(self, 'title'):
            verbose_name = self.title
        elif hasattr(self, 'filename'):
            verbose_name = self.filename
        else:
            verbose_name = self.__class__.__name__ + ' ' + str(self.id)
        return verbose_name