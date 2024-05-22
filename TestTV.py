# Program # 6; TestTv file

# Pseudocode

# Create the first TV Object labeled as 'tv1'
# Turn on 'tv1'
# Set 'tv1's channel to 30
# Set 'tv1's volume to 3
# Create the second TV Object labeled as 'tv2'
# Turn on 'tv2'
# Set 'tv1's channel to 3
# Set 'tv1's volume to 2
# Print 'tv1's channel and volume level
# Print 'tv2's channel and volume level

from TV import TV 

def TestTV():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)

