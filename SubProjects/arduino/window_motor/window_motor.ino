#define enA A1
#define m1h 8
#define m1l 9
#define b1 2
#define b2 3
int b1_value = 0;
int b2_value = 0;
void setup() {
  pinMode(enA, OUTPUT);
  pinMode(m1h, OUTPUT);
  pinMode(m1l, OUTPUT);
  pinMode(b1, INPUT);
  pinMode(b2, INPUT);
  Serial.begin(9600);
  // Set initial rotation direction
  //digitalWrite(in1, LOW);
  //digitalWrite(in2, HIGH);
}
void loop() {

  int pwmOutput = 500;  //Speed command
  int delaytime = 500; //Delay time, not used
  analogWrite(enA, pwmOutput); // Send PWM signal to L298N Enable pin
  b1_value = digitalRead(b1);
  b2_value = digitalRead(b2);
  if (b1_value==1 && b2_value ==0){
    digitalWrite(m1h, HIGH);
    digitalWrite(m1l, LOW);
  }
  else if (b1_value==0 && b2_value ==1){
    digitalWrite(m1h, LOW);
    digitalWrite(m1l, HIGH);
  }
  else{
    digitalWrite(m1h, LOW);
    digitalWrite(m1l, LOW);
  }
  Serial.print(b1_value);
  Serial.print(b2_value);
  Serial.println("loop");
  delay(delaytime);
  
  /*
  // Read button - Debounce
  if(b1_value == T
    digitalWrite(m1h, HIGH);
    digitalWrite(m1l, LOW);
    delay(delaytime);

    digitalWrite(m1h, LOW);
    digitalWrite(m1l, HIGH);
    delay(delaytime);
    */
}
