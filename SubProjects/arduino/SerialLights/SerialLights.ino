#include <FastLED.h>
#define NUM_LEDS 150
#define ledPin 7
#define LightEnablePin 2
#define b2 3
  int LightEnable;
  int b2_value;
  int x_color;
  int x_bright;
  int w;
  int color_ind;
  String serial_input;

CRGB leds[NUM_LEDS];
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Green, CRGB::Black};

void setup() {
  FastLED.addLeds<NEOPIXEL, ledPin>(leds, NUM_LEDS);
  Serial.begin(9600);
  FastLED.clear();
  pinMode(LightEnablePin, INPUT);
  pinMode(b2, INPUT);
  b2_value = 0;
  x_color = 0;
  x_bright = 50;
  w = 0;
}

void loop() {

  
  // Loop and conditional statement to control lights
  LightEnable = digitalRead(LightEnablePin);
  if (serial_input=="enable"){color_ind = 2;} 
  else{color_ind = 4;}
  while (w<= NUM_LEDS){
      leds[w] = ColorArray[color_ind];
      w = w + 1;
  }
  w = 0;

  if(Serial.available()){
        serial_input = Serial.readStringUntil('\n');
        Serial.print("You typed: " );
        Serial.println(serial_input);
  }

  
  FastLED.setBrightness(x_bright);
  FastLED.show();
  delay(500);
}
              
              
  
   


 
  
  
     
