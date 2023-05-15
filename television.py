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

# Define the main method for running the TV program
def main():
    # Use pyfiglet to print "TV Program" in ASCII art
    result = pyfiglet.figlet_format("TV Program", font="slant")
    print(result)

    # Create a TV instance
    tv = TV()

# Prompt the user to turn the TV on or off
    while True:
        choice = input("Enter 'on' to turn the TV on or 'off' to turn it off: ")
        if choice.lower() == 'on':
            tv.turnOn()
            break
        elif choice.lower() == 'off':
            tv.turnOff()
            break
        else:
            print("Invalid choice. Please enter 'on' or 'off'.")

    # Prompt the user to change the channel or adjust the volume level
    while tv.on:
        choice = input("Enter 'c' to change the channel, 'v' to adjust the volume level, or 'q' to quit: ")
        if choice.lower() == 'c':
            channel = int(input("Enter the channel number (1-120): "))
            tv.setChannel(channel)
            print(f"Current channel is {tv.getChannel()}")
        elif choice.lower() == 'v':
            volumeLevel = int(input("Enter the volume level (1-7): "))
            tv.setVolume(volumeLevel)
            print(f"Current volume level is {tv.getVolume()}")
        elif choice.lower() == 'q':
            tv.turnOff()
            break
        else:
            print("Invalid choice. Please enter 'c', 'v', or 'q'.")
    
# Call the main method to run the TV program



