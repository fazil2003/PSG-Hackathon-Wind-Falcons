# Data Science: Crime Analysis and Safety Recommendation
# Team Name: Wind Falcons

<img src="images/logo.png" />
<br>

### 🌟	What we have done
💫 We have analysed the dataset and <b>prepared the dataset</b> with necessary information.<br>
💫 We have plotted the <b>route</b> in the <a href="https://openstreetmap.org">OpenStreetMap.org</a> from the starting address to the destination address.<br>
💫 We have plotted the graph for total crimes based on the particular city for each year.<br>
💫 We have used <b>Autoregression</b> for time series analysis and prediction.<br>
💫 We have used <b>K Nearest Neighbors</b> for finding nearest places of crime occurences for each juncture between the routes.<br>
💫 We have used <b>Flask</b> to develop the web application to ease the process for the user.

### 🌟	Overview 
💫 First we perform exploratory data analysis on the given crime data then this data will be exported into the database for querying purposes. Then we use a standard navigation API to get the start(A) and end(B) destination thus we get the route from the point A to B. Now we get the reverse latitude from the points present in between A and B. For each and every point we perform caching so as to increase performance. Now that we got the latitude for every intermediate point we also have to get the crime’s location’s latitude. We perform K nearest neighbors for each point then display the results and ask for the user to change route if the route found has more crime as compared to other paths. 

### 🧭	Implementation details 
💫 The major features are that the analysis obtained can be further be displayed to the user like each crime in the intermediate area sorted based upon the recent to the oldest one. Tips for user to prevent the crime. Re-route if crime are less in alternative route. As we use K nearest neighbor instead of dijkstra for decreasing complexity. We use caching for every route until the database is updated/added by the admin. So this reduces complexity by a lot.

### 📱	Tools & Technologies 
💫 Python as the implementation language. Openrouteservice’s api for getting the Direction between two points (i.e) source and destination.  openstreetmap and requests for the location to latitude and longitude conversion.  K nearest points’s Algorithm for finding the closest crime for each intermediate point. Flask is to be used for web based application.

### 🌅	Screenshot 1
<img src="images/image1.png" style="width: 800px" /><br>
Starting Page of the Project. User needs to enter the starting and destination address.
<br>

### 🌅	Screenshot 2
<img src="images/image2.png" style="width: 800px" /><br>
Displays the shortest route first, then it reroutes to the alternative routes which has less crime occurence rate.
<br>

### 🌅	Screenshot 3
<img src="images/image3.png" style="width: 800px" /><br>
Plotted the predicted analysis.<br>

### 🐳  Requirements
💫 Python>=3.6

💫 base64<br>
💫 flask<br>
💫 io<br>
💫 matplotlib<br>
💫 numpy<br>
💫 pandas<br>
💫 pymongo<br>
💫 pymongo[src]<br>
💫 requests<br>
💫 sklearn<br>
💫 statsmodels<br>
💫 urllib<br>

#### 🧑🏻‍💻  Still Implementing
💫 Rerouting as per the crime rate.<br>
💫 Displaying the maximum crime that has occured in the particular region.<br>
💫 Adding safety recommendation to the users.<br>

#### 🤖 Team Members
<table>
  <tr>
    <td align="center"><a href="https://github.com"><img src="https://avatars.githubusercontent.com/u/45797873?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Janathsri Krishnan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/jfmengels"><img src="https://avatars.githubusercontent.com/u/75175772?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kaushik</b></sub></a><br /></td>
    <td align="center"><a href="https://jakebolam.com"><img src="https://avatars.githubusercontent.com/u/65252590?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohamed Fazil</b></sub></a><br /></td>
  </tr>
</table>

💫  20I224 - Kaushik S<br>
💫  21I433 - Janathsri Krishnan K<br>
💫  21I437 - Mohamed Fazil Z<br>