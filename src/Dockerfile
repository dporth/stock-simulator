FROM python:latest

RUN apt-get update
RUN apt install -y build-essential

RUN apt-get install -y curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN . ~/.bashrc
RUN apt-get install unixodbc-dev

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE  5000

RUN chmod a+x /app/uid_entrypoint.sh

# Run
ENTRYPOINT ["sh", "uid_entrypoint.sh"]