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

# Adding 2 tv instances
class TestTV:
    def main(self):
        tv1 = TV()
        tv2 = TV()
        
        # Prompt the user on channel and volume for both tv1 and tv2
        tv1.turnOn()
        channel1 = int(input("\033[32mEnter the channel for tv1 (1-120):\033[0m"))
        while not (1 <= channel1 <= 120):
            print("033[31mInvalid channel! Please enter a number between 1 and 120.\033[0m")
            channel1 = int(input("Enter the channel for tv1 (1-120): "))
        tv1.setChannel(channel1)

        volume1 = int(input("\033[32mEnter the volume level for tv1 (1-7):\033[0m"))
        while not (1 <= volume1 <= 7):
            print("033[31mInvalid volume level! Please enter a number between 1 and 7.\033[0m")
            volume1 = int(input("Enter the volume level for tv1 (1-7): "))
        tv1.setVolume(volume1)