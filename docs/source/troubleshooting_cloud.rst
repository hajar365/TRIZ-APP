Troubleshooting Guide for Cloud Version (Groq API)
======================================================

If you encounter any issues while using the **TRIZ Engineering Problem Solver** with the **Groq API (cloud)** version, try the following steps.

Common Issues:
--------------
1. **Groq API Key Not Working**  
- Ensure that your API key is correctly set in the `.streamlit/secrets.toml` file:
   
   ```
   [GROQ_API_KEY]
   api_key = "your-groq-api-key"
   ```

- If the key is incorrect or expired, generate a new one from the [Groq website](https://groq.com).

2. **Streamlit App Not Opening**  
- Ensure that all dependencies are installed by running:
   
   ```
   pip install -r requirements.txt
   ```

- Make sure no other application is using port 8501 (default Streamlit port).

3. **API Call Fails**  
- Ensure that the **Groq API key** is valid and has not exceeded any usage limits.
- Check for network connectivity issues when making API calls.

4. **Slow Performance**  
- If the app is running slow, it could be due to large models or heavy traffic on the Groq API servers. Try again later or reduce the number of API calls.

For additional support, please contact Groq support or refer to the [Ollama Troubleshooting Guide](troubleshooting_ollama).

5. **Model Not Responding**  
- Ensure that the Groq API is operational by checking their status page or contacting support.
- If the model fails to respond, try restarting the Streamlit app.
- If the issue persists, consider checking the Groq API documentation for any changes or updates.
