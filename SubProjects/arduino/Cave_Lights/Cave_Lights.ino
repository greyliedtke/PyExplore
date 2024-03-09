#include <FastLED.h>
#define NUM_LEDS 150
#define ledPin 7
#define b1 2
#define b2 3
  int b1_value;
  int b2_value;
  int x_color;
  int x_bright;
  int w;

CRGB leds[NUM_LEDS];
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Green, CRGB::Black};

void setup() {
  FastLED.addLeds<NEOPIXEL, ledPin>(leds, NUM_LEDS);
  Serial.begin(9600);
  FastLED.clear();
  pinMode(b1, INPUT);
  pinMode(b2, INPUT);
  b1_value = 0;
  b2_value = 0;
  x_color = 0;
  x_bright = 50;
  w = 0;
}

void loop() {
  // Read buttons
  b1_value = digitalRead(b1);
  b2_value = digitalRead(b2);

  
  // Change Color
  if (b1_value==1){
    x_color = x_color + 1;
    if (x_color > 4){
      x_color = 0;
    }
    delay(100);
  }

  // Change Brightness
  if (b2_value==1){
    x_bright = x_bright + 25;
    if (x_bright > 100){
      x_bright = 25;
    }
    delay(100);
  }

  // room lights   
  while (w<= NUM_LEDS){
    leds[w] = ColorArray[x_color];
    w = w + 1;
    //delay(100);
  }

  w = 0;
  FastLED.setBrightness(x_bright);
  FastLED.show();
  delay(500);
}
              
              
  
   


 
  
  
     
