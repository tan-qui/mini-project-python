try:
  import folium
  import pandas as pd
  import json
  import time

  print("\n================================Start================================\n")
  def drawMap(locations, staff):
    # Create a map centered at the first location
    mymap = folium.Map(location=[locations[0]["lat"], locations[0]["long"]], zoom_start=12)

    # Add markers and lines for each location
    for i, location in enumerate(locations):
        folium.Marker(
            location=[location["lat"], location["long"]],
            popup=location["address"],
            tooltip=f"Điểm {i+1}: {location['address']}",  # Add tooltip with address
        ).add_to(mymap)

        # Connect points with lines
        if i < len(locations) - 1:
            folium.PolyLine(
                locations=[[location["lat"], location["long"]],
                          [locations[i + 1]["lat"], locations[i + 1]["long"]]],
                color='blue'
            ).add_to(mymap)

    # Save the map to an HTML file
    mymap.save(f"map_{staff}.html")

  df = pd.read_excel("./data.xlsx")
  json_data = df.to_json(orient='table', force_ascii=False)
  load_data  = json.loads(json_data)
  array_data = load_data['data']

  if(len(array_data) == 0):
    print("Không tìm thấy dữ liệu !!!")
    print("\n================================End================================")
    time.sleep(5)
  first_staff = array_data[0]
  locations=[]
  for index, item in enumerate(array_data):
      if(item["staff"] != first_staff["staff"]):
        drawMap(locations, first_staff["staff"])
        locations=[]
        first_staff = item
      lo = {
        "address" : item["address"],
        "lat" : item["lat"],
        "long" : item["long"],
      }
      locations.append(lo)
      if(len(array_data) - 1 == index):
        drawMap(locations, first_staff["staff"])
        locations=[]
        first_staff = item
  print("Xem dữ liệu map..... trong cùng thư mục")
  print("\n================================End================================")
  time.sleep(5)
except Exception as bug:
  print(bug)
  print("\n================================End================================")
  time.sleep(5)