from httpclient import HttpClient
import json
'''
This is a python module which has computing functions interacts with external systems.
Computing Functions: It will interact with third party systems in order to compute the value.
'''


'''
This function calculates the altitude.
'''
def compute_altitude(lat, long):
    try:
        result = HttpClient.get(str(lat) + "," + str(long))
        result_json = json.loads(result.content.decode('utf-8'))
        if(result_json["statusCode"] == 200):
            return result_json['resourceSets'][0]["resources"][0]["elevations"][0],result_json["statusCode"],""
        else:
            return "", result_json["statusCode"], result_json['errorDetails']
    except Exception as e:
        print(e.message)


'''
This function calculates the timezone/local time.
'''
def compute_timezone(lat, long):
    try:
        result_time = HttpClient.get_resource("timezone", str(lat) + "," + str(long))
        result_json_time = json.loads(result_time.content.decode('utf-8'))
        if (result_json_time["statusCode"] == 200):
            return result_json_time['resourceSets'][0]["resources"][0]["timeZone"]['convertedTime']['localTime']
        else:
            return ""
    except Exception as e:
        print(e.message)