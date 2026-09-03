from django.db import models

class DeviceNode(models.Model):
    node_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.node_id} ({self.location})"

class SensorTelemetry(models.Model):
    node = models.ForeignKey(DeviceNode, on_delete=models.CASCADE, related_name='readings')
    temperature_c = models.FloatField()
    humidity_percent = models.FloatField()
    voltage_v = models.FloatField()
    is_alert = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
