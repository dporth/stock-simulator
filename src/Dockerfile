FROM python:latest

# Environment Variables
ARG database_account
ARG database_server
ARG database_password
ARG api_auth0_audience
ARG auth0_domain

ENV DATABASE_ACCOUNT=$database_account
ENV DATABASE_PASSWORD=$database_password
ENV DATABASE_SERVER=$database_server
ENV API_AUTH0_AUDIENCE=$api_auth0_audience
ENV AUTH0_DOMAIN=$auth0_domain

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

COPY . /src/
WORKDIR /src/

RUN pip install -r requirements.txt
RUN pip install uwsgi

EXPOSE  5000

RUN chmod a+x /src/uid_entrypoint.sh

# Run
ENTRYPOINT ["sh", "uid_entrypoint.sh"]