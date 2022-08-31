# 🤖Jarvis

#### It is a voice assistant. It can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.

![Jarvis](https://wallpapercave.com/wp/wp1913282.jpg)
  ---

## 📃 Installation
---
* Clone this repository in your local environment by running the code in your git bash.
  
```bash
git clone https://github.com/YOUR-USERNAME/Jarvis-python.git
```

Install the required **packages:**

* `pip install wolframalpha`

It requires an unique API key for every client. You have to signup and get your personal API key. Create your key from here [`Wolframalpha`](https://developer.wolframalpha.com/portal/myapps/)

Usage:

```python
import wolframalpha
client = wolframalpha.Client("uniquedid")
res = client.query()
results = next(res.results).text
```


* `pip install pyttsx3`

pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

Usage:

``` python
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```

* `pip install SpeechRecognition`

Library for performing speech recognition, with support for several engines and APIs, online and offline.

Usage:
``` python
import SpeechRecognition as sr

def takecommand():                   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recogizing...")
        query=r.recognize_google(audio)
        print(f"user Said {query}\n")

    except Exception as e:
        return "None"

    return query
```

* `pip install wikipedia`
  
Wikipedia API for Python

Usage:

```python
import wikipedia
print(wikipedia.summary("Metallica", sentences = 5))
```

* `pip install pywhatkit`
  
PyWhatkit is a simpe and powerful WhatsApp automation library with mant useful features.

Usage:

```python
import pywhatkit
# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("abcdef", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+911234567890", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("abcdef", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("abcdef", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("Enter Sandman")
```

* `pip install DateTime`

This package provides a DateTime data type, as known from Zope. Unless you need to communicate with Zope APIs, you're probably better off using Python's built-in datetime module.

Usage:
```python
import datetime

#Current Date and Time
print(datetime.datetime.now())

#Get Current Date
print(datetime.date.today())

#dir() function to get a list containing all attributes of a module.
print(dir(datetime))
```


* `pip install playsound`

Pure Python, cross platform, single function module with no dependencies for playing sounds.

```python
from playsound import playsound
playsound('/path/to/a/sound/file/you/want/to/play.mp3')
```
---
## 🏹 Features
- Wish user
- Tells about weather
- Open any website
- Tells about upcoming events
- Play music online
- Play vidoes on youtube
- Can do mathematical calculations
- Can tell latest news
- Open any software of your choice
- You can join your meetings fast using this
- Answer any generic questions
- Can tell you about any person via wikipedia
- It can shutdown your computer/laptop on yor command
- Can search any anything on google
- You can check your emails using this

  ---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
