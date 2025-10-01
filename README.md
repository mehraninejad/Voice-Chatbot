<h2>🎙&nbsp;Voice ChatGPT (Persian Supported) <h2>
<p>
This project is a simple voice-based chatbot that supports Persian language using SpeechRecognition and OpenAI GPT-4. You can speak into your microphone and receive intelligent responses from ChatGPT as text.
</p>
  
<br/>
<h2>🛠&nbsp;Features<h2>
<p>

🟢&nbsp;Recognizes Persian speech and converts it to text.
  <br/>
🟢&nbsp;Responds intelligently using gpt-4o-mini.
<br/>
🟢&nbsp;Reduces ambient noise with adjust_for_ambient_noise.
<br/>
🟢&nbsp;Timeout and phrase time limit for better usability.
<br/>
🟢&nbsp;Easy to extend and customize for your own projects.
</p>
<br/>
<h2>⚡&nbsp;Prerequisites<h2>
<p style="font-size:10px;"line-height:1.4;">
<b>Required libraries</b>
  
This project requires the following Python libraries:

☆&nbsp;openai
<br/>
☆&nbsp;SpeechRecognition
<br/>
☆&nbsp;python-dotenv

You can install all of them easily at once using the requirements.txt file:
```bash
pip install -r requirements.txt
```

<b>An OpenAI API key (place it in a config.env file):<b>
```bash
API_KEY=your_openai_api_key_here
```
 </p>
<br>
<h2>🎯&nbsp;How to Run</h2>

1. Create config.env and place your OpenAI key inside.

2. Run the script in Python:
```pthon
python voice_chatgpt.py
```
3. When you see Please speak..., start talking.

4.  Receives the response and saves it in a file called output.txt in the same folder as the script.
<br/>
<h3>Note about terminal display</h3>
<p>
- Persian text may appear reversed or disorganized when printed directly in the terminal due to right-to-left language issues.  
<br/>
- To solve this, the program automatically writes the output to output.txt, which can be opened in VSCode, Notepad++, or any text editor with UTF-8 support.
<br/>
- This ensures the Persian response is correctly formatted and readable.
<br/>
>Open output.txt to see the formatted Persian response.
</p>
<br/>
<h2>💚&nbsp;Outcome</h2> 

Running this project gives you a smart Persian voice chatbot that can be used for personal projects, learning, or fun.



