#YtDownloader
from pytube import YouTube
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err, intercept_stderr = stats.linregress(x, y)

print(slope)
print(intercept)
print(r)
print(p)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# try:
#     # Ask the user to input the YouTube URL
#     url = input("Enter the YouTube URL: ")
    
#     yt = YouTube(url)
    
#     print("Title:", yt.title)
#     print("Views:", yt.views)

#     # Get the highest resolution stream
#     yd = yt.streams.get_highest_resolution()
    
#     # Download the video to the current directory
#     yd.download()
    
#     print("Download complete.")
# except Exception as e:
#     print("An error occurred:", str(e))