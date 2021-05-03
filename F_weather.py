from random import randint
import csv 

def forecast_gen():
    rain_gen=sorted((randint(0,130),randint(0,130)))
    temp_gen=sorted((randint(-5,45),randint(-5,45)))
    wind_gen=sorted((randint(0,50),randint(0,50)))
    return(rain_gen,temp_gen,wind_gen)



def forecast():
    dic=[]
    turn=0
    for i in range(24):
        a,b,c=forecast_gen() ##check that a[0]!=a[1]
        while a[0]==a[1] or b[0]==b[1] or c[0]==c[1] or (a[1]-a[0])<40 or (b[1]-b[0])<25 or (c[1]-c[0])<25:
            a,b,c=forecast_gen()
            
        turn+=1
        dic.append(a+b+c+[turn])
    return(dic)

g=forecast()

#THIS CODE BELOW WOULD BE USEFUL IF YOU WANT TO CHECK, IN AN ORGANIZED CSV FILE, THE FORECAST FOR THE WHOLE GAME. (you would only need to pick a different name for the function above)
#"""





with open('data/weather.csv', 'w') as f: #its a matrix of 24 rows and 8 columns. each row represents data for one turn. First 2 columns are the temperature. Next 2 columns are the amount of rain range. Next 2 columns are the speed of wind range. Last 2 columns are range used for a random experiment resulting in a tornado.
    wtr = csv.writer(f)
    wtr.writerows(g)


def weatherinitializer(): #transform the csv file into a list of tuples  
    weather=[]
    b=0
    with open('data/weather.csv', 'r') as csv_file: #its a matrix of 24 rows and 8 columns. each row represents data for one turn. First 2 columns are the temperature. Next 2 columns are the amount of rain range. Next 2 columns are the speed of wind range. Last 2 columns are range used for a random experiment resulting in a tornado.
        csv_reader=csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            b=b+1
            a=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]) # b represents the turns. 24 in total
            weather.append(a)
    return (weather)
#"""



                    
                
def temperature(b,turn,a):
   for i in b:
       if turn==i[6]:
            c=randint(int(i[0]),int(i[1]))
            for z in a:
                z[2]=c
                
def wind (b,turn,a):
    for i in b:
        if turn==i[6]:
            c=randint(int(i[4]),int(i[5]))
            for z in a:
                z[3]=c

def rain (b,turn,a): # ( b , turns , a)
    for i in b: #weather initializer
        if turn==i[6]: #weather data for turn a
            c=randint(int(i[2]),int(i[3]))
            for z in a: # going over parcels #g=amount of rain accumulated till given turn 
                z[1]=c
 
                
                


