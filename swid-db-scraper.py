## https://iaspub.epa.gov/enviro/efservice/VIOLATION/ROWS/0:1000

import json
import functools
import requests
import logging
from xml.etree import ElementTree

# logging.basicConfig(
#     format='%(asctime)s %(levelname)-4s %(message)s',
#     level=logging.INFO,
#     datefmt='%H:%M:%S')

swdis_schema = None 

with open("json-schemas/SDWIS_schema.json") as schema:
    swdis_schema = json.load(schema)
    schema.close()


# example_url = "https://iaspub.epa.gov/enviro/efservice/VIOLATION/ROWS/0:1000"

# example_response = requests.get(example_url)

# tree = ElementTree.fromstring(example_response.content)
## if we can query the xml correctly we could build a url for each table
## then recursivly make calls until we have the entire table stored locally
## in some format.

## we are going to want some print outs so that we can keep track of how far we are
## with all the things

## to start we can just write to a csv file, later shift to databases
def build_base_url (table_name): #build url sans specific request for rows
    return "https://iaspub.epa.gov/enviro/efservice/" + table_name #+ '/ROWS/0:100'

def column_headers (json_table_schema):
    table_headers = []
    for key in json_table_schema['fields']:
        table_headers.append(key)
    return table_headers

def create_csv_row (table_headers, xml_object):
    csv_string = ''
    for header_name in table_headers:
        value = xml_object.find(header_name).text
        if value is None:
            csv_string += ''
        else:
            csv_string += '"' + value + '"'
        csv_string += ','
    return csv_string + '\n'



## examples
table_list = []

for key in swdis_schema:
    table_list.append(key)


first_table = table_list[0]
header_list = column_headers(swdis_schema[first_table])

first_url = build_base_url(first_table)
first_response = requests.get(first_url)
first_parsed_response = ElementTree.fromstring(first_response.content)

## containing directory
containing_directory = "data_pulls/swdis-data/"

## The errors seem to be inconsitant amongsht attempts at reproduction
## I have not yet pulled a full dataset however it seems as though
## the URL which Etree fails to parse is different each time.
## if after the error i manually retrieve the url and parse it,
## the xml parses correctly.

## My best guess here is that sometimes we get garbage XML and the best thing
## we can do is to just retry in those cases
def pull_table_to_csv (table_name, batch_size=10000, max_attempts=10, dir="raw_data/"):
    # open file connection
    filename = table_name + ".csv"
    filepath = containing_directory + filename
    file_object = open(filepath, 'w')

    #grab header info based off of json schema
    headers = column_headers(swdis_schema[table_name])

    ## concatenate & write out headers to the file
    file_object.write(','.join(map(str, headers)) + "\n")

    #build out the base url
    base_url = build_base_url(table_name)
    #curry fn to make a conversion fun that we can apply to xml nodes
    csv_conversion_fn = functools.partial(create_csv_row, headers)

    total_records = 0

    more_data = True
    while more_data:
        url_attempts = 0 # the number of times this URL has been attempted

        url = base_url + '/Rows/' + str(total_records) + ':' + str(total_records + batch_size - 1)
        print("using url ", url)

        try:
            xml_response = ElementTree.fromstring(requests.get(url).content)

            for record_element in xml_response:

                file_object.write(csv_conversion_fn(record_element))
                response_attributes = xml_response.attrib

                url_attempts = 0 # reset the counter 

                # if we get less than we expect we are done!
                if int(response_attributes['Count']) < batch_size: 
                    more_data = False

            total_records += int(response_attributes['Count'])
        except ElementTree.ParseError:
            print("Parse Error encountered, retrying URL")
            url_attempts += 1
            if url_attempts > max_attempts:
                print("max number of attempts exceeded, breaking out of loop")
                return


    file_object.close()
    print("done!")
    return

## if we have a function that could quickly figure out how many rows would be
## involved in generated the database then we could crunch it
## using separate processes to query the database in parallel, and just make a
## series of smaller files, then once all the requests are made we could just
## concatenate everything together. I would expect this to be quite a bit faster

## def find_db_row_count (table_name, batch_size=10000, max_attempts=10):

    





