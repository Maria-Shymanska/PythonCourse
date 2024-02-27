original_dict = {
    "The Legend of Zelda: Ocarina of Time": 1998,
    "Grand Theft Auto IV": 2008,
    "Red Dead Redemption": 2018,
    "Perfect Dark": 2000,
    "The Orange Box": 2007,
}


res = {}
for name, year in original_dict.items():
    if year > 2005:
        res[name] = year
        
print(res)

# lowercase titles
# select all after 2000 year
# select all in range

even_dict = {key: value for (key, value) in original_dict.items() if value % 2 == 0}
print(even_dict)
        