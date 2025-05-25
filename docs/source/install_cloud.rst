Installation Guide for Cloud Version (Groq API)
================================================

To install and run the **TRIZ Engineering Problem Solver** using **Groq API**, follow these steps.

Requirements:
-------------
- **Python 3.8+**
- **Streamlit** (for the web interface)
- **Groq API Key** (for accessing the Groq API)

Steps:
------
1. **Clone the Repository**  
   First, clone the repository to your local machine:
   
   ```
   git clone https://github.com/hajar365/TRIZ-APP.git
   cd your-repo
   ```

2. **Install dependencies**  
   Install the required Python packages:
   
   ```
   pip install -r requirements.txt
   ```

3. **Set Up Groq API Key**
   Sign up at Groq API and obtain an API key.
   Store your API key in the .streamlit/secrets.toml file. The file should look like this:
   
   ```
   [GROQ_API_KEY]
   api_key = "your-groq-api-key"
   ```

4. **Run the Streamlit App**  
   Finally, run the Streamlit app to start the TRIZ Engineering Problem Solver:
   
   ```
   streamlit run trizapp.py
   ```
   
   This will open the app in your web browser. You can now use the app for solving engineering problems using TRIZ methodology with Groq API.
 