import wave

filename = input("Please enter file name:")
wav = wave.open(filename, 'rb')

num_channels = wav.getnchannels()
sampwidth = wav.getsampwidth()
frame_rate = wav.getframerate()
num_frames = wav.getnframes()
cometype = wav.getcomptype()
compname = wav.getcompname()

print("num_channels=",num_channels)
print("sampwidth=",sampwidth)
print("frame_rate=",frame_rate)
print("num_frames=",num_frames)
print("cometype=",cometype)
print("compname=",compname)


wav.close
