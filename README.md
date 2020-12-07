# InstaUnfollow
A python program using selenium to check who is not following you back on Instagram.<br>
<h2>Dependencies</h2>
This script requires python3 and selenium installed.Download any version of python3 from <a href="https://www.python.org/downloads/">here.</a>For selenium just run the following code:<br>
```pip3 install selenium```
<br>
<h2>Setup</h2>
<br>
Firstly,download this script.
This script will only work if you have chrome.Download chromedriver from <a href="https://chromedriver.chromium.org/downloads">here.</a>
<br>
<i>Note:To use it with firefox change <br>```driver=webdriver.Chrome()```<br> in line 4 to<br>```driver=webdriver.Firefox()```<br>Then you should download the geckodriver from <a href="https://github.com/mozilla/geckodriver/releases">here.</a>
 </i>
 <br>
 After the download you should put the path of the driver in the file like this:<br>
 ```driver=webdriver.Chrome(r"C:\Users\aryas\Documents\chromedriver.exe")```
 <br>
After that put your username name and password in the file.
<br>
<h2>Run</h2>
Just run the script using python like:<br>
```python3 unfollow.py```
