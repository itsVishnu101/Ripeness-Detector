#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

const char* serverURL = "http://YOUR_SERVER_IP:8000/status";

#define RED_LED D1
#define GREEN_LED D2

void setup() {
  Serial.begin(9600);

  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    WiFiClient client;

    http.begin(client, serverURL);
    int httpCode = http.GET();

    if (httpCode == 200) {
      String payload = http.getString();
      Serial.println(payload);

      if (payload.indexOf("Ripe") != -1) {
        digitalWrite(GREEN_LED, HIGH);
        digitalWrite(RED_LED, LOW);
      } 
      else if (payload.indexOf("Unripe") != -1) {
        digitalWrite(RED_LED, HIGH);
        digitalWrite(GREEN_LED, LOW);
      } 
      else {
        digitalWrite(RED_LED, LOW);
        digitalWrite(GREEN_LED, LOW);
      }
    }

    http.end();
  }

  delay(5000);  // Poll every 5 seconds
}
