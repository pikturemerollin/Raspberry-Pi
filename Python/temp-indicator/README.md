# Temperature Indicator
A simple Python script that provides a visual indicator for the board temperature. When the board exceeds a defined threshold a red LED will light up, when it is below the threshold it will light a green LED.

## Requirements
Two LED bulbs will need to be wired to the GPIO pins. In this example I use pins 7 (green) and 11 (red) using the GPIO board mode.

## Configurations
You can customize the script to mean your needs. The two LED bulb pin numbers are defined by the variables **ledGreen** and **ledRed**.
The current threshold temperature for 'running warm/hot' is 135 degrees fahrenheit. This can be changed by editing the **highMark** variable.

## Use case
This was originally written to keep an eye on my board temperature for the RPi Zero W. But of course, do with it as you see fit.
