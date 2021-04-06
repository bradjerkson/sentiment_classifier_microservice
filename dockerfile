#Set ubuntu bionic
FROM ubuntu:bionic

#Update Ubuntu Packages, install Conda pre-reqs and a text editor
RUN apt-get update && \
    apt-get install -y nano wget bzip2 && \
    apt-get -y install sudo

#Add sudo group user "ubuntu" with no password
RUN adduser --disabled-password --gecos '' ubuntu && \
    adduser ubuntu sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/

#Set-up Flask Environment
WORKDIR /code
ENV FLASK_APP=flask_app.py
ENV FLASK_RUN_HOST=127.0.0.1
ENV FLASK_DEBUG=1

#Set up Anaconda environment
COPY environment.yml environment.yml
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh && \
    bash Anaconda3-2020.07-Linux-x86_64.sh -b

ENV PATH /home/ubuntu/anaconda3/bin:$PATH
RUN conda env create --name arqenv --file environment.yml
RUN exec bash && conda init bash && conda activate arqenv


COPY . .
#CMD ["flask", "run", "--port=80"]
#CMD ["python", "flask_app.py"]
#CMD ["conda", "run", "-n", "arqenv", "flask", "run"]
SHELL ["conda", "run", "-n", "arqenv", "/bin/bash", "-c"]
EXPOSE 80
ENTRYPOINT ["conda", "run", "-n", "arqenv", "python3", "flask_app.py"]
