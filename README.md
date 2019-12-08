### **Data**
Our squirrel sightings tracker uses Django development to create a Webapplication that tracks the squirrels in 2018 at Central Park. We had to import the squirrel census dataset from the city of new york. 
[2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

The user can add, edit and view some statistics on squirrel sightings. The user can also get a visualization of the squirrels location in Central Park on a map. 

### **To Install Dependencies**

```python
pip install -r requirements.txt
```

### **Views**
We have the followings Views:

1. Sightings 

A view that lists all the squirrel sightings with links to add and edit the sightings of the squirrels. Use /sightings to access 

2. Map 

A view that displays the locations of the squirrel sightings in Central Park on OpenStreets map. Use /map to access 

3. Update 

A view that updates a specific squirrel sighting. Add a squirrel unique ID to update the information of the squirrel. Use /sightings to access 

4. Add 

A view that creates a new squirrel sighting to our database. 


5. Stats 

A view that shows stats about some features on squirrel sightings. 
Use /sightings/stats to access 

### **Group Name and Section**
Group 58, Section 1 


### **UNI**
UNIs: [lvv2105, tsr2121, ef9873]


### **Link to the server**
