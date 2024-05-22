# This program is about an application of OOB; Program #6: Class (TV)

# Psuedocode

# Based from the presentation, do a TV Class file
# Set Class Attributes
    # 'channel' to integer (by default as 1)
    # 'volumeLevel' to integer (by default as 1)
    # 'on' to boolean ( by default as false)
# Initialize the attributes with the values
# Implement 'turnOn() to set 'on' to True
# Implement 'turnOff() to set 'on' to False
# Implement 'getChannel() to return to the current 'channel'
# Implement 'setChannel (channel)' to set the 'channel' if the TV is on 
    # Channel range should be within 1 to 120 
# Implement 'getVolume()' to return to current 'volumeLevel'
# Implement 'setVolume(volumeLevel)' to set the 'volumeLevel' if the TV is on
    # Volume range should be within 1 to 7
# Implement 'channelUp()' to increase the 'channel' by 1 
# Implement 'channelDown()' to decrease the 'channel' by 1
# Implement 'volumeUp()' to increase the 'volumeLevel' by 1
# Implement 'volumeDown()' to decrease the 'volumeLevel' by 1


class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on(self):
        self.on = True
    
    def turn_off(self):
        self.on = False
    
    def get_channel(self): 
        return self.channel
    
    def set_channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    
    def get_volume(self):
        return self.volume_level
    
    def set_volume(self, volume_level):
        if self.on and 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1
    
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1
    
    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1




