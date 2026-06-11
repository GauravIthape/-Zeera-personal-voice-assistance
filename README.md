# personal assistance


## 🧠 Project Overview: “Zeera – AI Voice Assistant”

**Purpose:**
Zeera is an **intelligent voice-controlled assistant** that listens to your voice commands, performs tasks like searching Wikipedia, opening websites, telling time, playing songs, cracking jokes, fetching news headlines, and more.

--- 

## ⚙️ Main Technologies Used

| Library                      | Purpose                                                     |
| ---------------------------- | ----------------------------------------------------------- |
| `pyttsx3`                    | Converts text to speech (lets Zeera “speak”).               |
| `speech_recognition`         | Captures and converts voice input to text.                  |
| `datetime`                   | Used to get the current time for greetings or telling time. |
| `wikipedia`                  | Fetches summaries from Wikipedia.                           |
| `webbrowser`                 | Opens websites in your default browser.                     |
| `os`                         | Accesses files, starts apps like music or VS Code.          |
| `pywhatkit`                  | Plays YouTube videos or songs.                              |
| `pyjokes`                    | Tells random jokes.                                         |
| `requests` + `BeautifulSoup` | Scrapes live news headlines from the web.                   |

---

## 🗣️ How Zeera Works (Step-by-Step Flow)

1. **Voice Initialization**

   * Uses `pyttsx3` to set the voice (female voice from `sapi5` engine).

2. **Greeting Function (`wishMe()`)**

   * Greets you according to the current time (Good Morning/Afternoon/Evening).
   * Introduces itself: “My name is Zeera. Please tell me how may I help you.”

3. **Listening Function (`takeCommand()`)**

   * Listens via the microphone using `speech_recognition`.
   * Converts your speech into text.
   * Prints and returns the recognized text.

4. **Main Assistant Loop (`run_assistant()`)**

   * Runs continuously and listens for commands.
   * Based on your voice input, it performs actions like:

---

## 💡 Key Features

| Command Example                                            | Action Performed                                           |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| “Search Elon Musk on Wikipedia”                            | Reads 2-sentence Wikipedia summary.                        |
| “Open YouTube”                                             | Opens YouTube in your browser.                             |
| “Open Google / Chrome / Spotify / ChatGPT / MSBTE website” | Opens respective site/application.                         |
| “Play music”                                               | Plays a local music file from `D:\music`.                  |
| “What’s the time?”                                         | Speaks the current system time.                            |
| “Play <song name>”                                         | Plays that song on YouTube using `pywhatkit`.              |
| “Tell me a joke”                                           | Says a random joke using `pyjokes`.                        |
| “News headline”                                            | Fetches and reads top headlines from *The Indian Express*. |
| “Shutdown” or “Exit”                                       | Thanks you and exits the program.                          |

---

---



## 🧩 Project Summary.

**Project Name:** Zeera – Voice Controlled Assistant
**Main Role:** Responds to voice commands and automates common desktop/internet tasks.
**Core Concept:** Human–Computer Interaction using Natural Language.
**Category:** Python-based AI / Automation project.
**Applications:**

* Personal assistant automation
* Accessibility support for visually impaired users
* Demonstration of speech recognition and web automation

