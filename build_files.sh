echo "BUILD START" 

python3.9 --version
python3.9 -m ensurepip 
python3.9 -m pip install -r requirements.txt 
python3.9 manage.py collectstatic

echo "GLIBC VERSION"
ldd --version

echo "INSTALL PLAYWRIGHT"
python3.9 -m playwright install
python3.9 -m playwright install-deps
apt-get install libnss3\libnspr4\libgbm1                                      

echo "playwright installed sucess"

#echo " MAKE MIGRATIONS..."
#python3.9 manage.py makemigrations --noinput
#python3.9 manage.py migrate --noinput

python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"