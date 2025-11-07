
install:	
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black . 3_matplotlib_e_streamlit/*.py

run:
	streamlit run 3_matplotlib_e_streamlit/3_3_stremalit_dashboard.py

lint:
	pylint --disable=R,C,W0622 3_matplotlib_e_streamlit/*.py

all: install lint format



