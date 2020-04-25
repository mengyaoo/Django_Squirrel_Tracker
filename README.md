Squirrel Sites Tracker in Central Park New York
====================================

<div align="center">
  <img src="https://github.com/zihui-zhou/Django_Project/blob/master/Squirrel_image.png"><br>
</div>

Description
-------------------
**Squirrel Tracker Final Project** is a web application in Django Framework to track all the known squirrel sites in Central Park of New York. Our source data is from [`2018 Central Park Squirrel Census data`](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). The users are allowed to add, update, and view squirrel data.

Main Features
-------------------
Here are just a few of the things that we do:
- Import and Export data using csv format: using management commands, we could import data from csv or output data from Django database into csv files. 

```sh
$ python manage.py import_squirrel_data /path/to/file.csv
```
```sh
$ python manage.py export_squirrel_data /path/to/file.csv
```
- View a map of all squirrel sites in Central Park. Located at `/map`
- See the list of all squirrel sites with their ID. Located at `/sightings`
- Add squirrel sites by clicking **Add** on sightings page. Located at `/sightings/add`
- Edit current squirrel sites. Located at `/sightings/<unique-squirrel-id>`
- See the statistics on current squirrel sites. Located at `/sightings/stats`

Contributors
-------------------
- Project Group 17
- UNIs: zz2694, mh4048

Link to run server
-------------------
- **Link to sightings**: https://squirrel-site-tracker.appspot.com/sightings/
- **Link to map**: https://squirrel-site-tracker.appspot.com/map/
