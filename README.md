# Task Management and Voice Interaction System

## Project Overview

This project implements a comprehensive task management and voice interaction system by integrating multiple scripts. The workflow covers everything from environmental noise detection, voice recording, voice-to-text conversion, text processing using a large language model, to text-to-speech synthesis.

## File Descriptions

### 1. `taskmng.py`

This is the current version of the task management script. It sequentially executes the following four scripts:

- **`testScanner.py`**  
  Utilizes a Fast Fourier Transform (FFT) to convert sound waves into numerical data and calculate a noise threshold. Any input that exceeds this threshold is recognized as the user’s voice input, triggering the recording process.

- **`audio2text.py`**  
  Uses the Vosk model to convert the recorded audio into text. The resulting text is saved into the file `manbo1.txt` for later use.

- **`testapi102.py`**  
  Reads content from `manbo1.txt` and processes the text input using the ChatGPT-3.5-turbo model, which is guided by a fixed prompt (documented in the submitted sketchbook on Canvas). The model’s response is then saved to `omajili1.txt` for subsequent processing.

- **`text2speech.py`**  
  Reads the content from `omajili1.txt` and uses the pyttsx3 model to convert the text into speech, which is then read aloud.

Together, these scripts form a complete automated workflow.

### 2. Additional Files

- **`testScannerTemp.py`**  
  A non-looping version of `testScanner.py`, designed to prevent CPU overload.

- **`tuskmng.py`**  
  A legacy task management script that was previously used for continuous loop execution.

- **`command.wav`**  
  The recording from the final presentation on March 5, 2025.

## How to Use

1. **Dependencies:**  
   Ensure that all required libraries are installed, including Vosk, pyttsx3, and access to the ChatGPT-3.5-turbo model.

2. **Execution:**  
   Run the `taskmng.py` script to start the complete task workflow.

3. **Workflow:**  
   The system will automatically:
   - Detect environmental noise and recognize voice input.
   - Record the user's command.
   - Convert the recorded voice to text.
   - Process the text with the ChatGPT-3.5-turbo model.
   - Convert the model’s response into audible speech.

## Notes

- Make sure that your microphone and speakers are functioning correctly to ensure optimal voice input and output quality.
- If you encounter performance issues, consider using `testScannerTemp.py` to reduce CPU load.

## Contribution Guidelines

Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request. Ensure that your changes align with the project's overall architecture and goals.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
