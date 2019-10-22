# faust-docker-compose

Step 1: `docker-compose up -d`

Step 2: Go inside any app `docker-compose exec app1 bash`

Step 3: Go inside app1 `docker-compose exec app1 bash` and run `faust --datadir=/data/work_6067 -A app worker -l info --web-port 6067`

Step 4: Go inside app1 `docker-compose exec app1 bash` and run `faust --datadir=/data/work_6067 -A app worker -l info --web-port 6067`

Inside any docker:
Step 5: `python test_put_topic` give some key and value

Step 6: `python test_read_topic` give some key and value

# Grafana setup

Step 1: Once Docker containers are up, go to **http://localhost:8000** (Grafana UI).

Step 2: Login with User: **admin**, Password: **admin**.

Step 3: Click on the icon in the upper left corner and select "**Data Sources**".

Step 4: Click on **Graphite**.

Step 5: In Name field, enter "**Statsd**", in Url field, enter: **http://localhost:8001** and in Access filed, choose "direct".

Step 6: Click "**Save & Test**". (The test should pass)

### Importing Dashboard

Step 1: In Grafana UI, click on the icon in the upper left corner and select "**Dashboards**" and click on "**Import**".

Step 2: Click on "**Upload .json File**"

Step 3: Select **faust_monitor_dashboard.json** file.

Step 4: Enter any name, and select "**Statsd**" as datasource.

Step 5: Click on "**Import**".
