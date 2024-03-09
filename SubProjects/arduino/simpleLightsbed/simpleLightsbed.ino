#include <FastLED.h>
#define NUM_LEDS 60
#define ledPin 2
#define ledPin3 3
CRGB leds[NUM_LEDS];
int p;
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Black,CRGB::Green};

void setup() {
  FastLED.addLeds<NEOPIXEL, ledPin>(leds, NUM_LEDS);
  FastLED.addLeds<NEOPIXEL, ledPin3>(leds, NUM_LEDS);
  pinMode(ledPin,OUTPUT);
  pinMode(ledPin3,OUTPUT);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
             int bright = 60;
             int color = 3;
              
                    int w = 0;                    
                    while (w<= 70){
                      leds[w] = ColorArray[0];
                      FastLED.setBrightness(bright);
                      w = w + 1;
                      //delay(100);
                      FastLED.show();
             }
}
              
  
   


 
  
  
     
