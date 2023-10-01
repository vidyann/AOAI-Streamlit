# Chat UI with StreamLit & Azure OpenAI
This sample helps with quick prototyping of conversational experience with Azure OpenAI using Streamlit. Streamlit is a Python library that allows you to create interactive & responsive web applications with few lines of code. 
You can run the code locally or deploy it to Azure Web Apps. 
1. Clone the repository & open it it VSCode.
2. To run it locally, execute below command in VSCode terminal
   streamlit run streamlitchatUI.py 
3. To deploy on Azure Web App
   Create a Python based Azure Web App from portal or VSCode.
   Add 
   python -m streamlit run streamlitUI.py --server.port 8000 --server.address 0.0.0.0
