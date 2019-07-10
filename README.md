# food
install Python 3.6 *sudo apt-get install python3.6*\
install pip  *sudo apt-get install pip* \
Create virtual environment with pip and python3 *python3 -m venv env*\
Activate environment like (source env/bin/activate)
Clone repository *git clone https://github.com/sureshkpiitk/TastySearch.git*\
Go to project cd TastySearch \
    Download dependencies (*pip install -r requirements.txt*)\
 **replace food/finefoods.txt with original finefoods.txt file**(I am not able to add file to github due to file size limit)\
 run server *command* **python3 manage.py runserver**\
Open browser and enter *http://localhost:8000/*
enter your query and limit and you will get your testy food search result\


If your system has low *RAM* then you can change the total review document by changing variable defined in food/view.py **MAX_LIMIT** (default 10000)


