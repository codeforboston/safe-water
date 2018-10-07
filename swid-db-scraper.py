## https://iaspub.epa.gov/enviro/efservice/VIOLATION/ROWS/0:1000

import json
import functools
import requests
import logging
import logging
import csv
import os

from xml.etree import ElementTree


# swdis_schema = None 

# with open("json-schemas/SDWIS_schema.json") as schema:
#     swdis_schema = json.load(schema)
#     schema.close()


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
    csv_row = []
    for header_name in table_headers:
        value = xml_object.find(header_name).text
        csv_row.append(value)
    return csv_row



## examples
table_list = []

for key in swdis_schema:
    table_list.append(key)


## containing directory
containing_directory = "data/"

if not os.path.exists(containing_directory):
    os.makedirs(containing_directory)

## The errors seem to be inconsitant amongsht attempts at reproduction
## I have not yet pulled a full dataset however it seems as though
## the URL which Etree fails to parse is different each time.
## if after the error i manually retrieve the url and parse it,
## the xml parses correctly.

## My best guess here is that sometimes we get garbage XML and the best thing
## we can do is to just retry in those cases
def pull_table_to_csv (
        table_json,
        table_name,
        batch_size=10000,
        max_attempts=10,
        dir="raw_data/",
        max_pulls=None):

    LOG_FILENAME = containing_directory + table_name + '.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

    # open file connection
    filename = table_name + ".csv"
    filepath = containing_directory + filename
    file_object = open(filepath, 'w')
    swdis_csv_writer = csv.writer(file_object)

    #grab header info based off of json schema
    headers = column_headers(table_json)

    ## concatenate & write out headers to the file

    swdis_csv_writer.writerow(headers)
    #build out the base url
    base_url = build_base_url(table_name)
    #curry fn to make a conversion fun that we can apply to xml nodes
    swdis_csv_conversion_fn = functools.partial(create_csv_row, headers)

    total_records = 0
    total_pulls = 0

    more_data = True
    while more_data:
        url_attempts = 0 # the number of times this URL has been attempted

        url = base_url + '/Rows/' + str(total_records) + ':' + str(total_records + batch_size - 1)
        logging.debug("using url " + url)
        print("using url ", url)

        try:
            url_response = requests.get(url).content
            if (not url_response): # empty response
                logging.debug("empty string response, no more data, breaking out of loop")
                print("empty string response, no more data, breaking out of loop")
                return
            xml_response = ElementTree.fromstring(requests.get(url).content)
            logging.debug('pulling additional records up too '+ str(total_records))

            for record_element in xml_response:
                swdis_csv_writer.writerow(swdis_csv_conversion_fn(record_element))

                response_attributes = xml_response.attrib
            logging.debug('Valid URL attempt')
            url_attempts = 0 # reset the counter

            total_pulls += 1 #increment total pulls
            # if we get less than we expect we are done!
            if int(response_attributes['Count']) < batch_size: 
                    more_data = False

            total_records += int(response_attributes['Count'])
            if (max_pulls is not None) and (max_pulls <= total_pulls):
                logging.debug('max pulls, breaking out of loop')
                print("max pulls, breaking out of loop")
                return
        except ElementTree.ParseError:
            logging.debug('Parse Error encountered, retrying URL')
            url_attempts += 1
            if url_attempts > max_attempts:
                logging.debug('max number of attempts exceeded, breaking out of loop')
                return


    file_object.close()

    logging.debug('done pulling table')
    print("done!")
    return

## takes a json structure referencing the a set of tables 
## and uses the information to scrap the data from the 
## epa site

def pull_json_tables(meta_json, max_pulls=None):
    for table_name in meta_json:
        pull_table_to_csv(meta_json[table_name], table_name, max_pulls=max_pulls)



#for table in table_list:
#    pull_table_to_csv(table)


## if we have a function that could quickly figure out how many rows would be
## involved in generated the database then we could crunch it
## using separate processes to query the database in parallel, and just make a
## series of smaller files, then once all the requests are made we could just
## concatenate everything together. I would expect this to be quite a bit faster

## def find_db_row_count (table_name, batch_size=10000, max_attempts=10):


# tri_facility_id_schema = None

# with open("schemas/TRI_Facility_Identification.json") as schema:
#     tri_facility_id_schema = json.load(schema)
#     schema.close()


def list_all_schemas(directory):
    json_schemas = []
    for file in os.listdir(directory):
        if file.endswith(".json"):
            json_schemas.append(file)
    return json_schemas

def pull_envirofacts_data (max_pulls=None):
    for schema_file in list_all_schemas("schemas"):
        schema_file_path = 'schemas/' + schema_file
        print("loading metadata from ", schema_file_path)
        with open(schema_file_path) as schema_file_object:
            meta_json = json.load(schema_file_object)
            print("retrieving associated data")
            pull_json_tables(meta_json, max_pulls=max_pulls)
    print("done pulling envirofacts data")


