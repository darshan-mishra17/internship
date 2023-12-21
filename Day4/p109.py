city=["Banglore",'hyderabad','goa','mumbai']
def length(city):
    return len(city)
city.sort(key=length)
print(city)