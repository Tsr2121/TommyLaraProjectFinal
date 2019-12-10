### **Data**
Our squirrel sightings tracker uses Django development to create a Webapplication that tracks the squirrels in 2018 at Central Park. We had to import the squirrel census dataset from the city of new york. 
[2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

The user can add, edit and view some statistics on squirrel sightings. The user can also get a visualization of the squirrels location in Central Park on a map. 

### **To Install Dependencies**

```python
pip install -r requirements.txt
```

### **App Name**

Our Project's name is squirreltracker and our App's name is tracking

### **Views**
We have the followings Views:

1. *Sightings* 

A view that lists all the squirrel sightings with links to add and edit the sightings of the squirrels. Use /sightings to access 


2. *Map* 

A view that displays the locations of the squirrel sightings in Central Park on OpenStreets map. Use /map to access. We have limited the showings of sightings to 50 to not freeze the server. 


3. *Update*

A view that updates a specific squirrel sighting. Add a squirrel unique ID to update the information of the squirrel. Use /sightings to access and click link of specific squirrel


4. *Add* 

A view that creates a new squirrel sighting to our database. Use /sightings/add


5. *Stats* 

A view that shows stats about some features on squirrel sightings. 
Use /sightings/stats to access 


### **Group Name and Section**
Group 58, Section 1 


### **Group Members**
Lara Vartanian (lvv2105), Tommy Rothman (tsr2121), Xuefeil Li (xl2915)


### **UNI**
UNIs: [lvv2105, tsr2121, xl2915]


### **Link to Github**
[Github Link](https://github.com/Tsr2121/TommyLaraProjectFinal.git)

Public Git Clone with HTTPS: https://github.com/Tsr2121/TommyLaraProjectFinal.git

### **Link to the server**

Link: https://tommy-lara-amy-tfa-project.appspot.com
* Add /sightings or /map to see


