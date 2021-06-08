import os ,pickle
from typing import Dict

parking_opt  =  int(input("Enter the option which you like to choose= \n1.Park your vehicle\n2.Collect your vehichle="))
amount_per_veh  =  25

count  =  0
if os.path.exists("parking_details.text"):
    vehicle_file =  open("parking_details.text","r")
    details  =  vehicle_file.readlines()
    for i in details:
        count  +=  1
    print(count)

else:
    pass

space  =  10
dic  =  {}

if parking_opt  ==  1:
    no_of_vehicle  =  int(input("Enter how many vehicle you want to park="))

    i  =  0
    while i  <  no_of_vehicle:

        if count  <=  space:
            vehicle  =  input("Enter which vehicle you want to park like(car,bike,scooty etc..) =")
            vehicle_num  =  input("Enter you vehicle number = ")
            time  =  input("Enter for how many hour you want to park you vehicle =")
            token_no  =  input("enter you token number=")

            dic["Vehicle"]  =  vehicle
            dic["num_of_vehicle"]  =  no_of_vehicle        
            dic["Vehicle_Number"]  =  vehicle_num
            dic["Time"]  =  time
            dic["Token"]  =  token_no

            file  =  open("parking_details.text","a+")
            data  =  file.write("\n")
            data  =  file.write(str(dic))

            file.close()

            print("********")
            print("Parking Succesfully \nPlease collect you Token")
            print("Your Token No is:=",token_no,"don not forget this")
            print("********")

        else:
            print("Try another parking area we dont have enough space")

        i  +=  1   
else:
    Token  =  input("enter your token number")
    return_time  =  input("enter the time=")
    charge  =  10

    def parse(d):
        dictionary  =  dict()
        # Removes curly braces and splits the pairs into a list
        pairs  =  d.strip('{}').split(', ')

        for i in pairs:
            pair  =  i.split(': ')
            # Other symbols from the key-value pair should be stripped.
            dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')

        return dictionary

    try:

        file_  =  open('parking_details.text', 'rt')
        lines  =  file_.read().split('\n')
        for data_ in lines:
            if data_  !=  '':
                dictionary  =  parse(data_)

            if  Token == dictionary["Token"] and  return_time !=  dictionary["Time"]:
                print("ye chal rah ahain")
                tax  =  amount_per_veh + charge
                charge_amount  =  int(return_time) -  int(dictionary["Time"])

                result  =  "you are late you have to give "+str(tax * charge_amount)
                break
            
            if Token != dictionary["Token"] and return_time != dictionary["Time"]:
                result  = "token and time not exits in parking information"
                
            else:
                result  =  "thank you your parking is done leave your byscile"

        print(result)
                    
        file_.close()
    except:
        print("Something unexpected occurred!")
