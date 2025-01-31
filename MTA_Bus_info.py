from config import MTA_API_KEY
import requests
bus_route = 'M5'  # Example bus route

# Endpoint for the MTA Bus Time API
url = f'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={MTA_API_KEY}&VehicleMonitoringDetailLevel=calls&LineRef={bus_route}'

response = requests.get(url)
data = response.json()

# Assuming the API and key are correct, this will print the data retrieved
print(data)