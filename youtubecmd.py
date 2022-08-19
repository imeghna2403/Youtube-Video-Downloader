from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
my_video = YouTube(link)

print("*****************PYTHON VIDEO DOWNLOADER*****************")

print("Title: ",my_video.title)
print("Number of views: ",my_video.views)
print("Length of video: ",my_video.length,"sec")
print("Rating of video: ",my_video.rating)
print(my_video.thumbnail_url) #to display thumbnail
videos = my_video.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("Enter serial no. for desired video quality  : ")) 
videos[strm].download()
print("Download Successful.")