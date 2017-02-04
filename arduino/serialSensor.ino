const int analogPin01 = 0;
int valPin01 = 0;

void setup(){
    Serial.begin(9600);//シリアル通信のレートを9600に設定
}

void loop(){
    valPin01 = analogRead(analogPin01);
}
