# build_files.sh
pip install -r requirements.txt --no-cache-dir -u
python3.9 manage.py collectstatic