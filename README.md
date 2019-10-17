# faust-docker-compose

Step 1: `docker-compose up -d`

Step 2: Go inside any app `docker-compose exec app1 bash`

Step 3: Go inside app1 `docker-compose exec app1 bash` and run `faust --datadir=/data/work_6067 -A app worker -l info --web-port 6067`

Step 4: Go inside app1 `docker-compose exec app1 bash` and run `faust --datadir=/data/work_6067 -A app worker -l info --web-port 6067`

Inside any docker:
Step 5: `python test_put_topic` give some key and value
Step 6: `python test_read_topic` give some key and value
