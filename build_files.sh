echo "BUILD START" 

python3.11.6 --version
python3.11.6 -m ensurepip 
python3.11.6 -m pip install -r requirements.txt 
python3.11.6 manage.py collectstatic --noinput --clear 

echo "INSTALL PLAYWRIGHT"
python3.11.6 -m playwright install

echo "BUILD END"