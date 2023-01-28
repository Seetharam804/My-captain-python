# My-captain-python

from bs4 import Beautifulsoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max",help = "Enter the total no of pages")
parser.add_argument("--dbname",help = "Enter the name of db",type = str)
args = parser.parse_args()

oyo_url= "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_Max = args.page_num_max
scraped_info_list = []
connect.connect(args.dbname)

for page_num in range(1,page_num_Max):
    url=oyo_url + str(page_num)
    print("Get requested for url:",url)
    req = requests.get(url)
    content = req.get(url)

    soup = BeatifulSoup(content, "html.parser")
    all_hotels = soup.find_all("Div", {"class" : "hotelCarListing"})

    for hotels in all_hotels:
        hotel_dic={}
        hotel_dic["name"]  = hotels.find("h3", {"class" : "listingHotelDesctription_hotelName" }).text
        hotel_dic["address"]= hotels.find('span', {"class" : "streetAddress"}).text
        hotel_dic["price"] = hotels.find("span", {"class" : "listing__finalPrice"}).text

        try:

            hotel_dict["rating"] = hotel.find("span", {"class" : "hotelRating ratingSummary"}).text

        except AttributeError:

             hotel_dict["rating"] = None

        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities_list = []

        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper_amenity"}):
            amenitieslist.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"] = '.'.join(amenities_list[:-1])


        scraped_info_list.append(hotel_dict)

        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

# print(hotel_name, hotel address, hotel price, hotel rating, amenities_list))

dataframe = pandas.DataFrame(scraped_info_list)

print("Creating csv file...")

dataFrame.to_csv("Oyo.csv")

connect.get_hotel_info(args.dbname)
