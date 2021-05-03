from data import constants 


def growth (a):
    
    for i in a:
        
        if i[0]==6:
            
            if abs(i[1]-constants.ideal_rain_av) < constants.ideal_rain_range_av:
                i[4]+=3
            if constants.ideal_rain_range_av < abs(i[1]-constants.ideal_rain_av) < constants.medium_rain_range_av:
                i[4]+=2
            if constants.medium_rain_range_av < abs(i[1]-constants.ideal_rain_av) < constants.min_rain_range_av:
                i[4]+=1
            if abs(i[1]-constants.ideal_rain_av) > constants.min_rain_range_av:
                i[4]-=1
                
                
            if abs(i[2]-constants.ideal_temp_av) < constants.ideal_temp_range_av:
                i[4]+=2
            if constants.ideal_temp_range_av < abs(i[2]-constants.ideal_temp_av) < constants.min_temp_range_av:
                i[4]+=1
            if abs(i[2]-constants.ideal_temp_av) > constants.min_temp_range_av:
                i[4]-=1
                
                
            if abs(i[3]-constants.ideal_wind_av) < constants.ideal_wind_range_av:
                i[4]+=1
            if abs(i[3]-constants.ideal_wind_av) > constants.ideal_wind_range_av:
                i[4]-=1

        elif i[0]==7:
            
            if abs(i[1]-constants.ideal_rain_m) < constants.ideal_rain_range_m:
                i[4]+=5 
            if constants.ideal_rain_range_m < abs(i[1]-constants.ideal_rain_m) < constants.medium_rain_range_m:
                i[4]+=3
            if constants.medium_rain_range_m < abs(i[1]-constants.ideal_rain_m) < constants.min_rain_range_m:
                i[4]+=2
            if abs(i[1]-constants.ideal_rain_m) > constants.min_rain_range_m:
                i[4]-=2
                
                
            if abs(i[2]-constants.ideal_temp_m) < constants.ideal_temp_range_m:
                i[4]+=4 
            if constants.ideal_temp_range_m < abs(i[2]-constants.ideal_temp_m) < constants.min_temp_range_m:
                i[4]+=3
            if abs(i[2]-constants.ideal_temp_m) > constants.min_temp_range_m:
                i[4]-=2
                
                
            if abs(i[3]-constants.ideal_wind_m) < constants.ideal_wind_range_m:
                i[4]+=3 
            if abs(i[3]-constants.ideal_wind_m) > constants.ideal_wind_range_m:
                i[4]-=1
                
                
        elif i[0]==8:
            
            if abs(i[1]-constants.ideal_rain_rf) < constants.ideal_rain_range_rf:
                i[4]+=7 
            if constants.ideal_rain_range_rf < abs(i[1]-constants.ideal_rain_rf) < constants.medium_rain_range_rf:
                i[4]+=5
            if constants.medium_rain_range_rf < abs(i[1]-constants.ideal_rain_rf) < constants.min_rain_range_rf:
                i[4]+=3
            if abs(i[1]-constants.ideal_rain_rf) > constants.min_rain_range_rf:
                i[4]-=4
                
                
            if abs(i[2]-constants.ideal_temp_rf) < constants.ideal_temp_range_rf:
                i[4]+=6 
            if constants.ideal_temp_range_rf < abs(i[2]-constants.ideal_temp_rf) < constants.min_temp_range_rf:
                i[4]+=4
            if abs(i[2]-constants.ideal_temp_rf) > constants.min_temp_range_rf:
                i[4]-=3
                
                
            if abs(i[3]-constants.ideal_wind_rf) < constants.ideal_wind_range_rf:
                i[4]+=5 
            if abs(i[3]-constants.ideal_wind_rf) > constants.ideal_wind_range_rf:
                i[4]-=2
                
                
def harvest (a,c,turn): 
    parcel=0
    for i in a:
        parcel+=1
        if i[0]==6:

            if i[4]==6 and (turn+1-i[5])==1:
                c[0]+=5
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if i[4]==6 and 2<=(turn+1-i[5])<=3:
                c[0]+=3
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if i[4]==6 and 4<=(turn+1-i[5])<=5:
                c[0]+=1
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if (turn+1-i[5])==6:    
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            
          
        elif i[0]==7:
            
            if i[4]==12 and (turn+1-i[5])==1:
                c[0]+=15
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if i[4]==12 and 2<=(turn+1-i[5])<=3:
                c[0]+=10
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if i[4]==12 and 4<=(turn+1-i[5])<=5:
                c[0]+=5
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if (turn+1-i[5])==6:
                c[0]-=1
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
        
        elif i[0]==8:
            
            if i[4]==18 and (turn+1-i[5])==1:
                c[0]+=30
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if i[4]==18 and 2<=(turn+1-i[5])<=3:
                c[0]+=20
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if i[4]==18 and 4<=(turn+1-i[5])<=5:
                c[0]+=10
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0
            if (turn+1-i[5])==6:
                c[0]-=5
                i[0]=None    
                i[1]=i[2]=i[3]=i[4]=i[5]=0


    