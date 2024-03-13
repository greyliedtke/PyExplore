#include <FastLED.h>
#define NUM_LEDS 60
#define NUM_LEDS2 60
#define change A7
#define ledPin 3
#define ledPin2 2
CRGB leds[NUM_LEDS];
CRGB leds2[NUM_LEDS2];
int p;int k;int kind=0; int whitelight; int w;
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Black,CRGB::Green};

void setup() {
  FastLED.addLeds<NEOPIXEL, ledPin2>(leds2, NUM_LEDS2);
  FastLED.addLeds<NEOPIXEL, ledPin>(leds, NUM_LEDS);
  pinMode(change,INPUT);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
              // room lights
             int changev = analogRead(change);
             int cave;
             int perimeter;
             int bright = 10;
Serial.println (changev);
              //1. Perimeter lights on
              if (changev<300){
                perimeter = 0;
                cave = 3;
                bright = 50;
              }
              //2. Perimeter diff colors
              if (changev<600&&(changev>300)){
                perimeter = 1;
                cave = 3;
              }
              //3. Both on
              if (changev<900&&(changev>600)){
                perimeter = 2;
                cave = 2;
              }
              //4. Full blast cave mode
              if (changev>900){
                perimeter = 3;
                cave = 0;
              }
                    w = 0;                    
                    while (w<= 70){
                      leds[w] = ColorArray[perimeter];
                      leds2[w] = ColorArray[cave];
                      //leds2[w] = CRGB::White;
                      FastLED.setBrightness(bright);
                      w = w + 3;
                      //delay(100);
                      FastLED.show();
                      
                    }
                    w = 0;
                    delay(1000);
                    Serial.println(changev);
             }
              
              
  
   


 
  
  
     
