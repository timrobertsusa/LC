# LC
sample repo with LangChain and python  

#### need to install the following  
pip install streamlit  
pip install streamlit-chat  
pip install langchain  
pip install python-dotenv  
pip install openai  

create a .env file outside of the view of git  
cd ..  
touch .env  


add the following name/value pairs    
OPENAI_API_BASE=  
OPENAI_API_KEY=  
OPENAI_API_VERSION="2023-07-01-preview"  
OPENAI_API_TYPE = "azure"  

Model Names  
In the the code, update for your model name and deployment name  

to run the file  
streamlit run main.py  
