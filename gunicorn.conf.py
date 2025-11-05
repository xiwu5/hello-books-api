# gunicorn.conf.py
import multiprocessing

# Gunicorn config variables
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120  # 2 minutes
bind = "0.0.0.0:10000"  # Use port 10000 as Render expects
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr
capture_output = True  # Capture print statements