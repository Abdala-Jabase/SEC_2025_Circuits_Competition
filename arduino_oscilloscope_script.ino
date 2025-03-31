int potPin = A3; // Potentiometer output connected to analog pin 3
int potVal = 0; // Variable to store the input from the potentiometer
int x;
int time=0;
// int time;
void setup() {
  Serial.begin(115200);     
  // Serial.setTimeout(1);      //  setup serial
}

void loop() {
  potVal = analogRead(potPin);  // read the input pin
  Serial.println(potVal);
  delay(50);
  time+=0.01;
  Serial.flush();
  // x=Serial.readString().toInt();      // debug value
}