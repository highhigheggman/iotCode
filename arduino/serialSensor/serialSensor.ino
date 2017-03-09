const int analogPin01 = A0;
int valPin01 = 0;

void setup() {
  //baud:9600, Even parity
  Serial.begin(9600, SERIAL_8E1);
}

void loop() {
  //read sensor val
  //valPin01 = analogRead(analogPin01);
  valPin01 = 1024;

  //send sensor val
  Serial.println(valPin01, DEC);

  Serial.flush();
  delay(300);
}
