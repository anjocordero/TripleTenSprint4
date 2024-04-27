# An Analysis of Vehicles on Sale in the US
URL for web application can be found at:
https://tripletensprint4-kehl.onrender.com/

This project aims to demonstrate the use of web application development and deployment, while using our existing data analysis techniques to find patterns in the data. We analyze a dataset of used vehicles on sale in the US.

## Libraries Used
- pandas
    - Used to import, modify, and organize data.
- plotly.express
    - Used to display graphs both in a Jupyter notebook and in the web application
- streamlit
    - Used to host the web application

## Instructions to run on your local machine
The web application is contained within `app.py`, and references the dataset `vehicles_us.csv`. If you want to host the application on your local machine, you'll need to install Python3, along with the libraries listed in `requirements.txt`.

Once all are installed, you can host the application by navigating to the project folder in a terminal, and running the command `streamlit run app.py`. Streamlit will then provide a URL where the application can be accessed.