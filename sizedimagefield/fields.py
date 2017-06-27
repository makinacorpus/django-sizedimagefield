import os

from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from django.utils.translation import ugettext_lazy as _


class SizedImageFieldFile(ImageFieldFile):
    def save(self, name, content, save=True):
        tmp = BytesIO()
        root, ext = os.path.splitext(content.name)
        image = Image.open(content.file)
        image.thumbnail((self.field.width, self.field.height), Image.ANTIALIAS)
        image.save(tmp, Image.EXTENSION[ext])
        tmp.seek(0)
        super(SizedImageFieldFile, self).save(name, File(tmp), save)


class SizedImageField(ImageField):
    attr_class = SizedImageFieldFile

    def __init__(self, verbose_name=None, width=None, height=None, **kwargs):
        if width is None or height is None:
            raise ValueError('width and height are required for SizedImageField.')
        self.width = width
        self.height = height
        kwargs.setdefault(
            'help_text',
            _('The picture will be resized to fit {width}px x {height}px.').format(
                width=width, height=height
            )
        )
        super(SizedImageField, self).__init__(verbose_name=verbose_name, **kwargs)
