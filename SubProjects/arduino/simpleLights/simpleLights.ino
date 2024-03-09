#include <FastLED.h>
#define NUM_LEDS 60
#define ledPin A5
CRGB leds[NUM_LEDS];
int p;
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Black,CRGB::Green,CRGB::Yellow};

void setup() {
  FastLED.addLeds<NEOPIXEL, ledPin>(leds, NUM_LEDS);
  pinMode(ledPin,OUTPUT);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
             int bright = 50;
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
              
  
   


 
  
  
     
