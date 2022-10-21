# build_files.sh
pip install --user -r requirements.txt --no-cache-dir -u
python3.9 manage.py collectstatic