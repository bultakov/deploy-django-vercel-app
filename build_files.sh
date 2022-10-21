# build_files.sh
pip install --user -r requirements.txt --no-cache-dir -U
python3.9 manage.py collectstatic