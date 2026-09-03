from django.contrib import admin
from .models import DeviceNode, SensorTelemetry
admin.site.register(DeviceNode)
admin.site.register(SensorTelemetry)
