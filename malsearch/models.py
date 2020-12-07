import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Sample(models.Model):
    sample_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=4096)
    hash_md5 = models.CharField(max_length=32, null=True)
    hash_sha1 = models.CharField(max_length=40, null=True)
    hash_sha256 = models.CharField(max_length=64, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_scanned = models.DateTimeField(null=True)
    file_size = models.IntegerField()


class SampleComment(models.Model):
    sample = models.ForeignKey(Sample, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.RESTRICT)
    comment = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)


class ScanResult(models.Model):
    scan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time_scanned = models.DateTimeField()
    file_type = models.CharField(max_length=1024, null=True)
    platform = models.CharField(max_length=1024, null=True)

    sample = models.ForeignKey(Sample, related_name='scan_results', on_delete=models.CASCADE)
