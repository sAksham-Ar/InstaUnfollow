# InstaUnfollow
A python program using selenium to check who is not following you back on Instagram.

## Dependencies

This script requires python3 and selenium installed.Download any version of python3 from <a href="https://www.python.org/downloads/">here.</a>For selenium just run the following code:

```
pip3 install selenium
```

## Setup

Firstly,download this script.
This script will only work if you have chrome.Download chromedriver from <a href="https://chromedriver.chromium.org/downloads">here.</a>

<i>Note:To use it with firefox change
 
 ```driver=webdriver.Chrome()```
 
 in line 4 to
 
 ```driver=webdriver.Firefox()```
 
 Then you should download the geckodriver from <a href="https://github.com/mozilla/geckodriver/releases">here.</a>
 </i>
 
 After the download you should put the path of the driver in the file like this:
 
 ```
 driver=webdriver.Chrome(r"C:\Users\aryas\Documents\chromedriver.exe")
 ```

After that put your username name and password in the file.

## Run

Just run the script using python like:

```
python3 unfollow.py
```
