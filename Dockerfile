FROM python:3 
ADD sysinfo.py /sysinfo.py
RUN pip3 install psutil datetime
RUN ["chmod", "+x", "/sysinfo.py"]
CMD ["python3", "./sysinfo.py"]