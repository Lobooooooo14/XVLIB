__author__ = "lobooooooo14"

import os
import json
import requests
import datetime
from bs4 import BeautifulSoup as BS

class Xvideos:
  def __init__(self, url=None, dl_path='./XVLIB download'):
    self.url = str(url)
    self.dl_path = str(dl_path)
 
 
  def get_video_id(url: str):
    return int(url.split('/')[3:][0].replace('video', ''))


  def download(self):
    html = BS(requests.get(self.url).text, 'html.parser')
    
    def get_video(html):
      external_player = html.find(id='html5video_base')
      
      videos = []
      for link in external_player.find_all('a'):
        videos.append(link.get('href'))
      
      return videos[-1]
    
    
    def name_video(html):
      return html.find(property="og:title").get('content')
    
    
    def save(video, path, name_file):
      if not os.path.exists(path):
        os.makedirs(path)
      
      dl = requests.get(video)
      
      with open(f'{path}/{name_file}.mp4', 'wb') as file:
        file.write(dl.content)
    
    
    save(get_video(html), self.dl_path, name_video(html))
    
    
  def info(self):
    html = BS(requests.get(self.url).text, 'html.parser')
    
    def convert(seconds): 
      return str(datetime.timedelta(seconds=int(seconds)))
    
    
    def get_video_name(html):
      return html.find(property="og:title").get('content')
    
    
    def get_thumbnail(html):
      return html.find(property="og:image").get('content')
    
    
    def get_comments_val(html):
      return int(html.find(class_='thread-node-children-count badge').string)
    
    
    def get_duration(html, is_converted=True):
      if is_converted == True:
        return convert(html.find(property="og:duration").get('content'))
      else:
        return int(html.find(property="og:duration").get('content'))
    
    
    def get_keywords(html):
      try:
        return html.find('meta', attrs={'name':'keywords'}).get('content').split(',')
      except AttributeError:
        return None

    
    def get_tags(html):
      try:
        tag = []
        div_area = html.find(class_="video-metadata video-tags-list ordered-label-list cropped")
        for i in div_area.find_all('a', attrs={'class':'btn btn-default'}):
          tag.append(i.get_text())
        return tag
      except AttributeError:
        return None
    
    
    def get_is_hd(html):
      try:
        if html.find(class_="video-hd-mark").get_text() == "1080p" or "720p":
          return True
      except AttributeError:
        return False
      
    
    def get_author_name(html):
      return html.find(class_="name").get_text()
    
    
    def get_is_verified(html):
      try:
        if html.find('span', attrs={'class':'icon-f icf-check-circle verified'}).get('title') == 'Verified uploader':
          return True
        
      except AttributeError:
        return False

    
    info_ = {
      'name':get_video_name(html),
      'duration':{
        'converted':get_duration(html, True),
        'brute':get_duration(html, False)
        },
      'author':{
        'name':get_author_name(html),
        'is_verified':get_is_verified(html)
        },
      'is_hd':get_is_hd(html),
      'video_id':Xvideos.get_video_id(self.url),
      'url':self.url,
      'keywords':get_keywords(html),
      'tags':get_tags(html),
      'thumbnail':get_thumbnail(html),
      'number_of_comments':get_comments_val(html)
    }
    
    return info_

