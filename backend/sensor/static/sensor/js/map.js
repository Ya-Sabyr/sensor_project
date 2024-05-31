document.addEventListener('DOMContentLoaded', (event) => {
    var map = L.map('map').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
 
    // Access the sensor data from the embedded JSON in the template
    var sensors = JSON.parse(document.getElementById('sensors-data').textContent);

// Create markers for each sensor
    sensors.forEach(function(sensor) {
        var marker = L.marker([sensor.coordinate_1, sensor.coordinate_2]).addTo(map)
            .bindPopup(sensor.address) // Assuming the Sensor model has a 'name' field
            .openPopup();
    });
});