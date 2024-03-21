#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytube


# In[4]:


from pytube import YouTube

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        
        stream = yt.streams.get_highest_resolution()
        
        save_location = "./downloads"
        
        stream.download(output_path=save_location)
        print("Video downloaded successfully!")
        
    except Exception as e:
        print("Error:", e)

video_url = input("Enter the YouTube video URL: ")
download_video(video_url)


# In[ ]:




