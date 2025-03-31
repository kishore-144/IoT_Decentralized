#include <WiFi.h>
#include <WebServer.h>

const char *ssid = "ESP_SoilSensor_2";
const char *password = "12345678";

WebServer server(80);

String getSoilMoistureStatus(int soilMoisturePin, int motorPin) {
    pinMode(motorPin, OUTPUT);
    int moistureValue = analogRead(soilMoisturePin);
    String motorState;
    
    if (moistureValue < 2500) {
        digitalWrite(motorPin, LOW);
        motorState = "Off";
    } else {
        digitalWrite(motorPin, HIGH);
        motorState = "On";
    }
    
    return "Soil Moisture: " + String(moistureValue) + ", Motor " + motorState;
}


void handleRoot() {
    server.send(200, "text/plain", getSoilMoistureStatus(34, 4)); 
}

void setup() {
    Serial.begin(115200);
    Serial.println("Sensor 2");
    WiFi.softAP(ssid, password);
    server.on("/", handleRoot);
    server.begin();
}

void loop() {
    server.handleClient();
    delay(10);
}
