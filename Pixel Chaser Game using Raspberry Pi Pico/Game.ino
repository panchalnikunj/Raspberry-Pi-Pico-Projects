#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
int  j;
#define BUTTON_PIN   14

#define PIN 28

#define NUMPIXELS 16 //NeoPixel ring size

#define BUZZER 4

int DELAY = 250;

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup()
{
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(BUZZER, OUTPUT);
#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
j = (random(0,15));
  pixels.begin();
}

void loop() {
  pixels.clear();
  runcode();

}

void runcode()
{
  for (int i = 0; i < NUMPIXELS; i++)
  {
    pixels.clear();
    pixels.setPixelColor(j, pixels.Color(255, 0, 0));
    pixels.setPixelColor(i, pixels.Color(0, 255, 0));

    pixels.show();

    delay(DELAY);

    if (digitalRead(BUTTON_PIN) == LOW && i == j)
    {
      wincode();
    }
    if (digitalRead(BUTTON_PIN) == LOW && i != j)
    {
      losecode();
    }
  }
}

void wincode()
{
  pixels.clear();
  j = (random(0,15));
  pixels.setPixelColor(0, pixels.Color(0, 255, 0));
  pixels.setPixelColor(1, pixels.Color(0, 255, 0));
  pixels.setPixelColor(2, pixels.Color(0, 255, 0));
  pixels.setPixelColor(3, pixels.Color(0, 255, 0));
  pixels.setPixelColor(4, pixels.Color(0, 255, 0));
  pixels.setPixelColor(5, pixels.Color(0, 255, 0));
  pixels.setPixelColor(6, pixels.Color(0, 255, 0));
  pixels.setPixelColor(7, pixels.Color(0, 255, 0));
  pixels.setPixelColor(8, pixels.Color(0, 255, 0));
  pixels.setPixelColor(9, pixels.Color(0, 255, 0));
  pixels.setPixelColor(10, pixels.Color(0, 255, 0));
  pixels.setPixelColor(11, pixels.Color(0, 255, 0));
  pixels.setPixelColor(12, pixels.Color(0, 255, 0));
  pixels.setPixelColor(13, pixels.Color(0, 255, 0));
  pixels.setPixelColor(14, pixels.Color(0, 255, 0));
  pixels.setPixelColor(15, pixels.Color(0, 255, 0));
  pixels.setPixelColor(16, pixels.Color(0, 255, 0));
  pixels.show();
  if (DELAY > 25)
  {
    DELAY = DELAY - 25;
  }
  if (DELAY == 25)
  {
    DELAY = 250;
    rainbow(10);
  }
  delay(500);
}

void losecode()
{
  pixels.clear();
  DELAY = 250;
  j = (random(0,15));
  pixels.setPixelColor(0, pixels.Color(255, 0, 0));
  pixels.setPixelColor(1, pixels.Color(255, 0, 0));
  pixels.setPixelColor(2, pixels.Color(255, 0, 0));
  pixels.setPixelColor(3, pixels.Color(255, 0, 0));
  pixels.setPixelColor(4, pixels.Color(255, 0, 0));
  pixels.setPixelColor(5, pixels.Color(255, 0, 0));
  pixels.setPixelColor(6, pixels.Color(255, 0, 0));
  pixels.setPixelColor(7, pixels.Color(255, 0, 0));
  pixels.setPixelColor(8, pixels.Color(255, 0, 0));
  pixels.setPixelColor(9, pixels.Color(255, 0, 0));
  pixels.setPixelColor(10, pixels.Color(255, 0, 0));
  pixels.setPixelColor(11, pixels.Color(255, 0, 0));
  pixels.setPixelColor(12, pixels.Color(255, 0, 0));
  pixels.setPixelColor(13, pixels.Color(255, 0, 0));
  pixels.setPixelColor(14, pixels.Color(255, 0, 0));
  pixels.setPixelColor(15, pixels.Color(255, 0, 0));
  pixels.setPixelColor(16, pixels.Color(255, 0, 0));
  pixels.show();
  digitalWrite(BUZZER, HIGH);
  delay(500);
  digitalWrite(BUZZER, LOW);
}

void rainbow(int wait) 
{
  for(long firstPixelHue = 0; firstPixelHue < 3*65536; firstPixelHue += 256) {
    for(int i=0; i<pixels.numPixels(); i++) { 
      int pixelHue = firstPixelHue + (i * 65536L / pixels.numPixels());
      pixels.setPixelColor(i, pixels.gamma32(pixels.ColorHSV(pixelHue)));
    }
    pixels.show();
    delay(wait);
  }
}
