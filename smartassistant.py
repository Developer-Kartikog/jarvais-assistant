import datetime
import webbrowser
import wikipedia
from googletrans import Translator
import requests

def speak(text):
    """Print instead of speak for text-based interaction."""
    print(f"> {text}")

# Feature: Fetch News
def get_news(topic):
    """Open Google search for the latest news on a given topic."""
    query = f"latest news about {topic}"
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Showing news articles about {topic}.")

# Feature: Translate Text
def translate(text, source_language, target_language):
    """Translate text from source language to target language."""
    translator = Translator()
    try:
        translation = translator.translate(text, src=source_language, dest=target_language)
        translated_text = translation.text
        speak(f"Translation: {translated_text}")
        return translated_text
    except Exception as e:
        speak(f"Error during translation: {e}")
        return None

# Feature: Calculator
def calculator(expression):
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)
        speak(f"The result is: {result}")
        return result
    except Exception as e:
        speak(f"Error evaluating expression: {e}")
        return None

# Feature: Wikipedia Search
def search_about(topic):
    """Search Wikipedia for a topic and return a summary."""
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak(f"According to Wikipedia: {summary}")
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"The topic is ambiguous. Suggestions: {e.options[:5]}")
        return None
    except wikipedia.exceptions.PageError:
        speak("Sorry, no page was found for the given topic.")
        return None
    except Exception as e:
        speak(f"An error occurred: {e}")
        return None

# Feature: Current Time
def tell_time():
    """Provide the current time."""
    now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {now}.")
    return now

# Feature: Contact Support
def contact_support():
    """Provide contact details for support."""
    support_details = """
    For any issues or queries, feel free to reach out:
    - Email: developerkartik7@gmail.com
    - Documentation: www.jarvais-docs.com
    - GitHub: github.com/jarvais-assistant
    """
    speak(support_details)


# New Feature: Fetch Weather
def get_weather(city):
    """Fetch the current weather for a city."""
    api_key = "your_openweather_api_key"  # Replace with your actual API key.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            speak(f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius.")
        else:
            speak(f"Could not fetch weather data for {city}: {data['message']}.")
    except Exception as e:
        speak(f"An error occurred while fetching weather data: {e}")

# New Feature: To-Do List
todo_list = []

def add_task(task):
    """Add a task to the to-do list."""
    todo_list.append(task)
    speak(f"Task added: {task}")

def view_tasks():
    """View all tasks in the to-do list."""
    if todo_list:
        speak("Here are your tasks:")
        for i, task in enumerate(todo_list, start=1):
            speak(f"{i}. {task}")
    else:
        speak("Your to-do list is empty.")

def remove_task(index):
    """Remove a task from the to-do list by index."""
    try:
        task = todo_list.pop(index - 1)
        speak(f"Task removed: {task}")
    except IndexError:
        speak("Invalid task number.")

# Example Usage
def main():
    speak("Welcome! How can I assist you today?")
    # Add examples of how to interact with these features.

if __name__ == "__main__":
    main()
