
<div align="center"> 
  <img src="https://img.shields.io/github/last-commit/Lobooooooo14/XVLIB?color=blue&style=for-the-badge">
  <img src="https://img.shields.io/github/repo-size/Lobooooooo14/XVLIB?style=for-the-badge">
  <img src="https://img.shields.io/github/commit-activity/w/Lobooooooo14/XVLIB?style=for-the-badge">
  <img src="https://img.shields.io/github/languages/top/Lobooooooo14/XVLIB?logo=Python&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/github/v/release/Lobooooooo14/XVLIB?color=brightgreen&style=for-the-badge">
  <img src="https://img.shields.io/github/license/Lobooooooo14/XVLIB?style=for-the-badge">
  <img src="https://www.codefactor.io/repository/github/lobooooooo14/xvlib/badge" alt="CodeFactor">
</div>

***

<div align="center">
  <p><i>A simple Python package to scrape information or download videos from xvideos.com</i></p>
</div>

<div align="center">
  <h1>XVLIB</h1>
  <ul>
    <li>don't need cookies :cookie:</li>
    <li>no need to login :bust_in_silhouette:</li>
    <li>don't need tokens  :key:</li>
  </ul>
  <br>
  <p><b>supports pages:</b></p>
  <br>
  <ul>
    <li>heterosexual :man: :woman:</li>
    <li>gay :rainbow_flag:</li>
    <li>transsexual :transgender_flag: </li>
  </ul>
</div>

***

<div align="center">
  <h2>installation</h2>
</div>

```sh
pip install git+https://github.com/Lobooooooo14/XVLIB.git
```
<div align="center">
  <h2>how to import:</h2>
</div>

```python
import XVLIB

x = XVLIB.Xvideos()
```
<div align="center">
  <p>or</p>
</div>

```python
from XVLIB import Xvideos

x = Xvideos()
```
<div align="center">
  <h2>use:</h2>
  <p><b>how to use XVLIB to get video information in a dictionary format:</b></p>
</div>

```python
from XVLIB import Xvideos

x = Xvideos()

x.url = 'video url goes here'

print(x.info())
```

<div align="center">
  <p><b>example response:</b></p>
</div>

```python
{
  'name': 'video name', 
  'duration': {
    'converted': '0:05:02', 
    'brute': 302
   }, 
  'author': {
    'name': 'autor name', 
    'is_verified': False
  }, 
  'is_hd': False, 
  'video_id': 00000000, 
  'url': 'https://www.xvideos.com/video00000000/video_name', 
  'keywords': [
    'xvideos', 
    'xvideos.com', 
    ' x videos', 
    'x video', 
    'porn', 
    'video', 
    'videos', 
    'sexy'
  ], 
  'tags': [
    'sexy'
  ], 
  'thumbnail': 'http://img-hw.xvideos-cdn.com/videos/photo.jpg', 
  'number_of_comments': 7
}
```

<div align="center">
  <p><b>and to download the video too:</b></p>

> if no download location is passed, a folder named `XVLIB download` in your code directory will be created.
</div>

```python
from XVLIB import Xvideos


x = Xvideos()

x.url = 'video url goes here'

x.download('./optional path to download')
```
