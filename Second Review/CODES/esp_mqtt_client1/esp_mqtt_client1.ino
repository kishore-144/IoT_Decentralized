#include <WiFi.h>
#include <WebServer.h>

const char *ssid = "ESP_SoilSensor_1";
const char *password = "12345678";

WebServer server(80);

void handleRoot() {
    server.send(200, "text/plain", "Soil Moisture: 45%");
}

void setup() {
    Serial.begin(115200);
    Serial.println("Sensor 1");
    WiFi.softAP(ssid, password);
    server.on("/", handleRoot);
    server.begin();
}

void loop() {
    server.handleClient();
}
