#include <FastLED.h>
#define NUM_LEDS 150
#define DATA_PIN A5
int Motion = 2;
CRGB leds[NUM_LEDS];
int p;int k;int kind=0; int whitelight;
int m;int prev;
void setup() {
  pinMode(Motion, INPUT);
  pinMode(DATA_PIN, OUTPUT);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
  // put your main code here, to run repeatedly:
  m = digitalRead(Motion);
  if (m != prev){
    Serial.println(m);
  }
  prev = m;
  //delay(1000);
  //Serial.println(m);
}
