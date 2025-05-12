Installation Guide for Local Version (Ollama)
=============================================

To install and run the **TRIZ Engineering Problem Solver** locally using **Ollama** and the **LLaMA3** model, follow these steps.

Requirements:
-------------
- **Python 3.8+**
- **Ollama** (for running the LLaMA3 model locally)
- **Streamlit** (for the web interface)

Steps:
------
1. **Clone the Repository**  
   First, clone the repository to your local machine using Git:
   
   ```
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
   
2. **Install dependencies**  
   Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. **Install Ollama**  
   To run the LLaMA3 model locally, you need to install Ollama. Follow these steps:
   Go to the Ollama website and download the appropriate version for your operating system (macOS, Windows, or Linux).
   Follow the installation instructions on the website to install Ollama.
4. **Download the LLaMA3 Model**  
   After installing Ollama, download the LLaMA3 model using the following command:

   ```
   ollama pull llama3
   ```

5. **run the llama3 model**

   ```
   ollama run llama3
   ```   

6. **Run the Streamlit App**  
   Finally, run the Streamlit app to start the TRIZ Engineering Problem Solver:

   ```  
   streamlit run localtrizzapp.py
   ```

    This will open the app in your web browser. You can now use the app locally for solving engineering problems using TRIZ methodology.

