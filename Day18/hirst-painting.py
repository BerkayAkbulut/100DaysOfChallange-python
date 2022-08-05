import colorgram

colors=colorgram.extract("photo.jpg",25)
first_color=colors[0]
rgb=first_color.rgb
print(rgb)
for _ in range(len(colors)):
    color=colors[_]
    rgb = color.rgb
    print(rgb)
