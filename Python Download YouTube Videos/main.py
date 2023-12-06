from pytube import YouTube

link = input("Paste the Link")
print("Downloading....")

YouTube(link).streams.first().download()
print("Video Downloaded Sucessfully")