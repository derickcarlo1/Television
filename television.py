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
            print("Invalid channel! Please enter a number between 1 and 120.")
            channel1 = int(input("\033[32mEnter the channel for tv1 (1-120):\033[0m"))
        tv1.setChannel(channel1)

        volume1 = int(input("\033[34mEnter the volume level for tv1 (1-7):\033[0m"))
        while not (1 <= volume1 <= 7):
            print("Invalid volume level! Please enter a number between 1 and 7.")
            volume1 = int(input("\033[34mEnter the volume level for tv1 (1-7):\033[0m"))
        tv1.setVolume(volume1)

        tv2.turnOn()
        channel2 = int(input("\033[32mEnter the channel for tv2 (1-120):\033[0m"))
        while not (1 <= channel2 <= 120):
            print("Invalid channel! Please enter a number between 1 and 120.")
            channel2 = int(input("\033[32mEnter the channel for tv1 (1-120):\033[0m"))
        tv2.setChannel(channel2)

        volume2 = int(input("\033[34mEnter the volume level for tv1 (1-7):\033[0m"))
        while not (1 <= volume2 <= 7):
            print("Invalid volume level! Please enter a number between 1 and 7.")
            volume2 = int(input("\033[34mEnter the volume level for tv1 (1-7):\033[0m"))
        tv2.setVolume(volume2)  
        
        # Display the current channel and volume of respective tv
        print(f"\033[33mtv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}\033[0m")
        print(f"\033[33mtv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}\033[0m")

        # Ask the user if they want to repeat the process
        while True:
            repeat = input("Do you want to change the TV settings again? (y/n): ")
            if repeat.lower() != "y":
                print("\033[38;5;202m5Goodbye!\033[0m")
                break

            channel1 = self.get_valid_input("\033[32mEnter the channel for tv1 (1-120): \033[0m", 1, 120)
            tv1.setChannel(channel1)

            volume1 = self.get_valid_input("\033[34mEnter the volume level for tv1 (1-7): \033[0m", 1, 7)
            tv1.setVolume(volume1)

            channel2 = self.get_valid_input("\033[32mEnter the channel for tv2 (1-120): \033[0m", 1, 120)
            tv2.setChannel(channel2)

            volume2 = self.get_valid_input("\033[34mEnter the volume level for tv2 (1-7): \033[0m", 1, 7)
            tv2.setVolume(volume2)

            # Display the current channel and volume of respective tv
            print(f"\033[33mtv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}\033[0m")
            print(f"\033[33mtv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}\033[0m")

    def get_valid_input(self, prompt, min_value, max_value):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print("Invalid input! Please enter a valid value.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

# Calling the main method
if __name__ == '__main__':
    COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

# Generate the Figlet text
figlet_text = pyfiglet.figlet_format("TV Setup Program")

# Apply color to the Figlet text
colored_figlet_text = COLOR_RED + figlet_text + COLOR_RESET

# Print the colored Figlet text
print(colored_figlet_text)

TestTV().main()