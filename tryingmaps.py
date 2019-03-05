import googlemaps
# Requires API key 
gmaps = googlemaps.Client(key="YOUR API KEY")

# Requires cities name
x=input("enter boarding point:")
y=input("Enter Destination:")
origin=gmaps.geocode(address=x)
destination=gmaps.geocode(address=y)
x_placeid=origin[0]['place_id']
y_placeid=destination[0]['place_id']

#print Distance and Time taken to travel
#my_dist = gmaps.distance_matrix(x,y)['rows'][0]['elements'][0]
#print("The Distance Between",x,"and",y,"is:",my_dist['distance']['text'],"& The time taken to travel is:",my_dist['duration']['text'])

#opening html file
file=open("maps.html","w+")
file.write('<iframe\n')
file.write('width="600" height="450"\n')
file.write('frameborder="0" style="border:0"\n')
file.write('src="https://www.google.com/maps/embed/v1/directions?\n')
file.write('origin=place_id:')
file.write(x_placeid)
file.write('&destination=place_id:')
file.write(y_placeid)
file.write('&key=AIzaSyBKhnCDuVGNjktDW6suR6IXgA1imlgmZaA" allowfullscreen>\n')
file.write('</iframe>')
file.close()

#Opening Direction webpage 
import webbrowser
webbrowser.open('maps.html') 
