import requests
'''
 Http wrapper
'''

class HttpClient:


    @staticmethod
    def get(payload):
        try:
            result = requests.get('http://dev.virtualearth.net/REST/v1/Elevation/List?points=' + payload + '&'
                                                'key=Av0tRD9CWVpc7FTrPaewewnZ-hwgwPbTAnHZ3c6rod2tltVgthQ682NvjsV__xJC')
            return result
        except Exception as e:
            raise e

    @staticmethod
    def get_resource(resource, payload):
        try:
            result = requests.get('http://dev.virtualearth.net/REST/v1/'+resource+'/' + payload + '?'
                                                'key=Av0tRD9CWVpc7FTrPaewewnZ-hwgwPbTAnHZ3c6rod2tltVgthQ682NvjsV__xJC')
            return result
        except Exception as e:
            raise e
