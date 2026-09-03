from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DeviceNode, SensorTelemetry
import json

def index(request):
    if DeviceNode.objects.count() == 0:
        DeviceNode.objects.create(node_id="NODE-LAB-01", location="Server Rack A")
        DeviceNode.objects.create(node_id="NODE-LAB-02", location="Classroom 101")
        
    nodes = DeviceNode.objects.all()
    readings = SensorTelemetry.objects.order_by('-timestamp')[:15]
    return render(request, 'sensors/index.html', {'nodes': nodes, 'readings': readings})

@csrf_exempt
def ingest_data(request, node_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8') or '{}')
        node = DeviceNode.objects.get(node_id=node_id)
        temp = float(data.get('temp', 25.0))
        hum = float(data.get('humidity', 50.0))
        volt = float(data.get('voltage', 3.3))
        alert = temp > 40.0 or volt < 3.0
        
        SensorTelemetry.objects.create(node=node, temperature_c=temp, humidity_percent=hum, voltage_v=volt, is_alert=alert)
        return JsonResponse({"status": "logged", "alert": alert})
    return JsonResponse({"error": "POST required"}, status=405)
