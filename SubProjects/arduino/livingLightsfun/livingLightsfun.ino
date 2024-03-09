#include <FastLED.h>
#define NUM_LEDS 60
#define DATA_PIN 9
#define switcher 7
CRGB leds[NUM_LEDS];
int ledPin = 7; // select the pin for the LED
int p;int k;int kind=0; int whitelight;
int previousSound; int alternator; int blinker;int avgDiff;
CRGB::HTMLColorCode ColorArray[] = {CRGB::Red,CRGB::Blue,CRGB::Green,CRGB::Purple,CRGB::Aqua};
CRGB::HTMLColorCode ColorArray2[] = {CRGB::Red,CRGB::Black,CRGB::Blue};

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(switcher, INPUT);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  Serial.begin(9600);
  FastLED.clear();
}

void loop() {
  
  k = 0;
  whitelight = digitalRead(switcher);
  if(whitelight == 1){
    kind = 69;
  }
  CRGB::HTMLColorCode c = ColorArray[p];//set color
      p = p+1;
      if(kind == 0){
     //middle out
        while(k <= 29){    
            leds[k+30] = c;
            leds[29-k] = c;
            k = k+1;
            leds[k+30] %= 100;
            leds[29-k] %= 100;
            FastLED.show();
            delay(50);
                  }
                  }
       //OUT to in
       else if (kind == 1){
        while(k <= 29){    
            leds[k] = c;
            leds[59-k] = c;
            k = k+1;
            leds %= 100;
            FastLED.show();
            delay(50);
                  }
       }
       else if (kind == 69){
        while(k <= 59){
          leds[k+1] = CRGB::Black;
          leds[k] = CRGB::White;
          k = k+1;
          FastLED.show();
                  }
       }
                  
if (p>4){ //reset color index if run out of colors
    p = 0;
    kind = kind+1;
    if (kind>1){
      kind = 0;
    }
        }
 delay(400);
 Serial.println(switcher);
}
