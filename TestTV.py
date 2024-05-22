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
# Call 'TestTv' function to execute the script

from TV import TV 

def TestTV():
    tv1 = TV()
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume(3)

    tv2 = TV()
    tv2.turn_on()
    tv2.set_channel(3)
    tv2.set_volume(2)

    print(f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
    print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")

TestTV()