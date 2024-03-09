#include <FastLED.h>
#define NUM_LEDS 150
#define NUM_LEDS2 60
#define change A7
#define DATA_PIN 9
#define ledPin 7
#define otherled 5
CRGB leds[NUM_LEDS];
CRGB leds2[NUM_LEDS2];
int p;int k;int kind=0; int whitelight; int w;
int previousSound; int alternator; int blinker;int avgDiff;
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Black,CRGB::Green};

void setup() {
  FastLED.addLeds<NEOPIXEL, otherled>(leds2, NUM_LEDS2);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  pinMode(change,INPUT);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
              // room lights
             int changev = analogRead(change);
             int below;
             int bed;
             int bright = 20;
              
              if (changev<300){
                below = 0;
                bed = 3;
                bright = 40;
              }
              if (changev<600&&(changev>300)){
                below = 2;
                bed = 2;
              }
              if (changev<900&&(changev>600)){
                below = 3;
                bed = 1;
              }
              if (changev>900){
                bed = 1;
              }
                    w = 0;                    
                    while (w<= 90){
                      leds[w] = ColorArray[bed];
                      leds2[w] = ColorArray[below];
                      leds2[w] = CRGB::White;
                      FastLED.setBrightness(bright);
                      w = w + 2;
                      //delay(100);
                      FastLED.show();
                      
                    }
                    w = 0;
                    Serial.println(bed);
             }
              
              
  
   


 
  
  
     
