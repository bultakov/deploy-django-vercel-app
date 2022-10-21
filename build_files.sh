# build_files.sh
pip install -r requirements.txt --no-cache-dir -U
python3.9 manage.py collectstatic --noinput