Troubleshooting Guide for Local Version (Ollama)
================================================

If you encounter any issues while using the **TRIZ Engineering Problem Solver** with the **Ollama (local)** version, try the following steps.

Common Issues:
--------------
1. **Ollama Installation Issues**  
   - Ensure that you have followed the installation steps on the [Ollama website](https://ollama.com).
   - Restart your computer after installation to ensure that the Ollama command is recognized.

2. **Model Not Running**  
   - Ensure that the model is properly downloaded by running:
     
     ```
     ollama pull llama3
     ```

   - If the model fails to load, try running:
     
     ```
     ollama run llama3
     ```


3. **Streamlit App Not Opening**  
   - If the app fails to open, check if all dependencies are correctly installed by running:
     
     ```
     pip install -r requirements.txt
     ```

   - Ensure that no other application is using port 8501 (default Streamlit port).

4. **No API Response**  
   - Ensure that the **Ollama model** is running in the background before launching the Streamlit app.
   - If necessary, restart the model with:
     
     ```
     ollama run llama3
     ```
     

If none of these solutions resolve your issue, please consult the [Groq API Troubleshooting Guide](troubleshooting_groq_api).
