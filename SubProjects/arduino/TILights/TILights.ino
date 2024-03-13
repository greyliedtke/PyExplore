#include <FastLED.h>
#define NUM_LEDS 50
#define led1 6
#define led2 7
  int LightEnable;
  int b2_value;
  int x_color;
  int x_bright;
  int w;
  int color_ind;
  String serial_input;

#define NUM_STRIPS 2
#define NUM_LEDS_PER_STRIP 50
CRGB leds[NUM_STRIPS][NUM_LEDS_PER_STRIP];
CRGB::HTMLColorCode ColorArray[] = {CRGB::White,CRGB::Blue,CRGB::Red,CRGB::Green, CRGB::Black};

void setup() {
  FastLED.addLeds<NEOPIXEL, led1>(leds[0], NUM_LEDS_PER_STRIP);
  FastLED.addLeds<NEOPIXEL, led2>(leds[1], NUM_LEDS_PER_STRIP);
  Serial.begin(9600);
  FastLED.clear();
  // pinMode(LightEnablePin, INPUT);
  // pinMode(b2, INPUT);
  x_bright = 50;
}

void set_color(int color, char strip, int brightness = 20) {
  color = 2;
  for(int x = 0; x < 10; x++)
    //strip[x] = ColorArray[color];
    Serial.println(strip);
  }
  FastLED.setBrightness(brightness);
  FastLED.show();
}


void loop() {
  // Loop and conditional statement to control lights
  //LightEnable = digitalRead(LightEnablePin);
  // if (serial_input=="enable"){color_ind = 2;} 
  // else{color_ind = 4;}
  FastLED.setBrightness(x_bright);
  
// This outer loop will go over each strip, one at a time
  for(int x = 0; x < 2; x++) {
    // This inner loop will go over each led in the current strip, one at a time
    for(int i = 0; i < NUM_LEDS; i++) {
      leds[x][i] = ColorArray[1];
      FastLED.show();
      //leds[x][i] = CRGB::Black;
      delay(10);
    }
  }


  if(Serial.available()){
        serial_input = Serial.readStringUntil('\n');
        Serial.print("You typed: " );
        Serial.println(serial_input);
  }
}
              
              
  
   


 
  
  
     
