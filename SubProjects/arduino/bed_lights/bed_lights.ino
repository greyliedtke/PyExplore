#include <FastLED.h>
#define NUM_LEDS 150
#define NUM_LEDS2 60
#define ledPin 7

CRGB leds[NUM_LEDS];
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Black,CRGB::Green};

void setup() {
  FastLED.addLeds<NEOPIXEL, ledPin>(leds, NUM_LEDS);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
              // room lights
             int bright = 100;
             int w = 0;      
             while (w<= 90){
                      leds[w] = ColorArray[0];
                      w = w + 1;
                      //delay(100);
                    }
                    w = 0;
                    FastLED.setBrightness(bright);
                    FastLED.show();
                    Serial.println('hey');
             }
              
              
  
   


 
  
  
     
