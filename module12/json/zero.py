import json


# load - deserialization from files
# loads - deserialization from object
# dump - deserialization in file
# dumps - deserialization in place

# curl https://jsonplaceholder.typicode.com/posts/
# wget -O-  https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)