# another py for testtv class
from TV import TV

# 2 instances TV
tv1=TV()
tv2=TV()

# default settings for TV1
tv1.setChannel(30)
tv1.setVolume(3)
# default settings for TV2
tv2.setChannel(3)
tv2.setVolume(2)

# Print default settings for TV 1 and 2
print("tv1's channel is",tv1.getChannel(),
      "and volume level is",tv1.getVolume())

print("tv2's channel is",tv2.getChannel(),
      "and volume level is",tv2.getVolume())