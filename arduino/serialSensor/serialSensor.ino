const int analogPin01 = A0;
int valPin01 = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  //read sensor val
  //valPin01 = analogRead(analogPin01);

  valPin01 = valPin01 + 2;
  //send sensor val
  Serial.println(valPin01, DEC);
  Serial.flush();
  delay(300);
}
