#include <FastLED.h>
#define NUM_LEDS 150
#define DATA_PIN A5

CRGB leds[NUM_LEDS];
int p;int k;int kind=0; int whitelight;


void setup() {
  pinMode(DATA_PIN, OUTPUT);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {

  
  k = 0;
  while(k <= 150){    
            leds[k] = CRGB::White;
            k = k+1;
            //leds[k] %= 10;
            FastLED.setBrightness(75);
            FastLED.show();
            delay(10);
  }
}
