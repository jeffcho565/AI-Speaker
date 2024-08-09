# AI Speech Recognition and Response System

This project demonstrates a simple AI system that listens to user input, processes speech-to-text, and responds accordingly with text-to-speech output. The system is built using Python and utilizes the `speech_recognition` library for capturing and recognizing speech, the `gTTS` library for converting text to speech, and the `playsound` library to play the generated audio files.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Functions](#functions)
  - [record()](#record)
  - [ai_answer()](#ai_answer)
  - [speach(file_name)](#speach)
  - [main()](#main)
- [License](#license)

## Requirements

To run this project, you need the following Python libraries:

- `speech_recognition`
- `gTTS`
- `playsound`
- `os`
- `datetime`

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment using the following command:

    ```bash
    python -m venv myenv
    ```

3. Activate the virtual environment:

    - On Windows:
    
        ```bash
        myenv\Scripts\activate
        ```

    - On macOS and Linux:
    
        ```bash
        source myenv/bin/activate
        ```

4. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can install the required libraries individually:

    ```bash
    pip install speechrecognition gtts playsound
    ```

## Usage

1. Ensure that your microphone is properly connected and recognized by your system.
2. Run the `test_AI.py` script:

    ```bash
    python test_AI.py
    ```

3. The AI will begin listening for your voice input. Speak commands clearly into the microphone.
4. To ask for the current date and time, say "what is the date and time".
5. To exit the program, say "close".

## File Structure

- `test_AI.py`: The main script containing the AI functions and logic.
- `requirements.txt`: A file listing the required Python libraries.
- `myenv/`: The virtual environment directory containing the installed dependencies.

## Functions

### `record()`

This function listens to the user's voice input and converts it to text using Google's speech recognition service. The recognized text is saved to `sample.txt`.

### `ai_answer()`

This function reads the recognized text from `sample.txt` and checks if it matches the query "what is the date and time". If so, it responds with the current date and time, and saves this response back to `sample.txt`. The response is then converted to speech using the `speach()` function. If the recognized text doesn't match the query, it prompts the user with "How can I help you further?".

### `speach(file_name)`

This function reads text from a specified file and converts it to speech using the Google Text-to-Speech (gTTS) library. The resulting audio file is played using the `playsound` library and then deleted.

### `main()`

The main loop that continuously listens for user input, processes it, and generates appropriate responses until the user says "close", which ends the program.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
