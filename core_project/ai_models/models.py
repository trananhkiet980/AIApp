from django.db import models
from django.urls import reverse

class AiModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên Mô hình AI")
    framework = models.CharField(max_length=50, verbose_name="Nền tảng (VD: TensorFlow)")
    description = models.TextField(verbose_name="Mô tả chức năng")

    def get_absolute_url(self):
        return reverse('ai_list')