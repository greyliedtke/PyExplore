// Sketch to learn about transistors as switches...
#define test_bo 53


void setup() {
  // put your setup code here, to run once:
  pinMode(test_bo, OUTPUT);
  
  // Create serial connection
  Serial.begin(9600);

  
}

void loop() {
  
  // put your main code here, to run repeatedly:
  digitalWrite(test_bo, HIGH);
  delay(1000);
  digitalWrite(test_bo, LOW);
  delay(1000);

}
