# Import the pyfiglet module for ASCII art
import pyfiglet

# Define the TV class
class TV:
    # Initialize the TV with default values
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    # Turn the TV on
    def turnOn(self):
        self.on = True

    # Turn the TV off
    def turnOff(self):
        self.on = False

    # Get the current channel
    def getChannel(self):
        return self.channel

    # Set the current channel
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    # Get the current volume level
    def getVolume(self):
        return self.volumeLevel

    # Set the current volume level
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    # Increase the channel by one
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    # Decrease the channel by one
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    # Increase the volume level by one
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    # Decrease the volume level by one
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1

# Define the TestTV class
class TestTV:
    # Define the main method for running the TV program
    def main(self):
        # Use pyfiglet to print "TV Program" in ASCII art
        result = pyfiglet.figlet_format("TV Program", font="slant")
        print(result)     

# Create two TV instances

# Turn on TV 1, set the channel and volume

# Turn on TV 2, increase the channel twice and volume once

# Print the current channel and volume for both TVs

# Run the TestTV program

