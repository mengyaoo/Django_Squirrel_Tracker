Squirrel Tracker in Central Park New York
====================================

<div align="center">
  <img src="https://github.com/zihui-zhou/Django_Project/blob/master/Squirrel_image.png"><br>
</div>

Description
-------------------
**Squirrel Tracker** is a web application built in Django Framework to track all known squirrels in Central Park in Manhattan, New York City, NY. Our source data is from [`2018 Central Park Squirrel Census`](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). Users can add, update, and view squirrel data on the web application. 

Main Features
-------------------
What we have accomplished:
- Import and Export data using csv format: using management commands, we could import data from csv or output data from Django database into csv files. 

```sh
$ python manage.py import_squirrel_data /path/to/file.csv
```
```sh
$ python manage.py export_squirrel_data /path/to/file.csv
```
- View a map of all squirrels in Central Park. Located at `/map`
- See the list of all squirrel sites with their ID. Located at `/sightings`
- Add squirrel sites by clicking **Add** on sightings page. Located at `/sightings/add`
- Edit current squirrel sites. Located at `/sightings/<unique-squirrel-id>`
- See the statistics on current squirrel sites. Located at `/sightings/stats`

Contributors
-------------------
- Project Group 17: Zihui Zhou, Mengyao He
- UNIs: zz2694, mh4048

Website
-------------------
- http://34.86.107.55/admin/
- http://34.86.107.55/sightings/
- http://34.86.107.55/map/
