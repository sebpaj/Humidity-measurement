#include <dht.h>

#define DHT11_PIN 7
#define ANALOG_PIN A0
dht DHT;
float temp;

void setup(){

  Serial.begin(9600);
  delay(500);
  Serial.println("DHT11 Humidity & temperature Sensor \n\n");
  delay(1000);
}

void loop(){
  temp = analogRead(ANALOG_PIN);
  temp = temp *0.48828125;
  Serial.print("LM35 temperature = ");
  Serial.print(temp);
  Serial.print("*C ");
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("DHT11 humidity = ");
  Serial.print(DHT.humidity);
  Serial.print("%");
  Serial.print(", DHT11 temperature = ");
  Serial.print(DHT.temperature);
  Serial.println("*C ");
  delay(5000);
}

