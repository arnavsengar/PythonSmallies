from pytube import YouTube
link=input("Enter Link: ")
vid=YouTube(link)
stream=vid.streams.get_highest_resolution()
stream.download()