from PIL import Image
import ast
"""
!!!!!! in order for program to work maps 1-5 .png must be in the same folder as .this file as well as folder(preferably empty) name maps!!!!!
(revrites anything with same name as files created in list_of_pix() and disc())
done for jirka to read image so he could put it in pandemic java application
1
list_of_pix
creates two txt files with list of pixeles of image in first file in format color (x,y) = (R,G,B)
and second file with each line being a command adding in java language (x,y) into allowed set 
expects image in same directory with its name as filename attribute
allowed_list expects list of tuples of colors that should be accesibe
saves them in same directory this ntrophy.py file is in
1.5
disc()
creates and saves a circle into a png file
2
run multiple maps()runs for maps 1-5 and saves in folder maps
3
read allowed_colors for barvy.txt in same directory as ntrophy.py file reads and puts into list allowed colors
only if barvy.txt is in forma e.g
(181,230,29) (241,193,29) (239,228,176)
(255,201,14) (195,195,195)
meaning:- line per map
        - spaces between tuples
"""

def read_allowed_colors(file_name):         # see above 3
    list_of_colors = []
    with open (file_name) as farben:        
        for line in farben:
            line = line.rstrip("\n")
            list_per_map = line.split(" ")
            to_list_of_colors = []
            for x in list_per_map:
                x= ast.literal_eval(x)                  #makes a tuple x in str type tuple representation e.g: (1,2,3)
                to_list_of_colors.append(x)
            list_of_colors.append(to_list_of_colors)
    print(list_of_colors)
    return(list_of_colors)
            
         
def run_multiple_maps(map_list=["map1","map2","map3","map4","map5"]):           # see above 2
    al_list = read_allowed_colors("barvy.txt")  #[[(181,230,29),(241,193,29),(239,228,176)],[(255,201,14),(195,195,195)],[(181,230,29)],[(181,230,29),(112,146,190)],[(195,195,195)]]
    for i in range (len(map_list)):
        list_of_pix(str(map_list[i])+".png",al_list[i],i)


def list_of_pix(filename, allowed_list = [(220,120,30)],i = 1):                 # see above 1
    im = Image.open(filename)
    map_list=["map1","map2","map3","map4","map5"]
    im = im.convert("RGB")
    width, height = im.size
    exp = open("maps/ntrophy_export_{}".format(map_list[i]), "w")         #name of  file will be e.g ntrophy_export_map1
    allowed = open("maps/ntrophy_allowed_{}".format(map_list[i]), "w")    #name of  file will be e.g ntrophy_allowed_map1
    for x in range(width):
        for y in range(height):
            pix_tup=im.getpixel((x,y))
            position = "({},{})".format(x,y)
            if pix_tup in allowed_list:
                allowed.write("allowed ({},{})\n".format(x,y))
            pix_tup = str(pix_tup)
            pix_tup = pix_tup.replace(" ","")
            exp.write("color " + position + " = " + str(pix_tup)+"\n")   
    allowed.close            
    exp.close   
#list_of_pix("map1.png")

def disc(a = 120, r = 50):              #a width and height of pic, r== radius of circle    see above 1.5
    im = Image.new("RGB", (a,a), (255,255,255))
    for x in range(a):
        for y in range(a):
            if (x-a/2)**2 + (y-a/2)**2 < r**2:
                im.putpixel((x, y), (220,120,30))
            else:
                im.putpixel((x,y), (0,0,255))
    im.save("alfa.png")                                     
#disc()

run_multiple_maps()            
