## the original webscraper depended on the schemas scraped from the web inorder to
## determine which values it should query the xml responses for. This caused problems
## when the schemas where either unreliable or had slight language descrepancies between the
## xml tags. the alternative approach in this script will be to use the xml as the only source of
## data

## algorithm description
## query restful API to view all XML
## scrape xml for header names, then for each xml record print out a corresponding row in a file
## -- add row number to record when we print out the files
## once we have scraped all XML for a given table, we need too add headers to the file
##

import functools # vote reduce back into the standard libarary!
import requests
import logging
import csv
import os
import logging
import multiprocessing as multi

#from multiprocessing import Manager
from xml.etree import ElementTree

# create the logger
logger = logging.getLogger('epa-data-scraper')
logger.setLevel(logging.DEBUG)
# create file hander which logs debug messages
fh = logging.FileHandler('epa-webscraper.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

max_query_attempts = 10 # number of times we will try a url before giving up on it
def query_restful_api(url, previous_attempts):
    """Query the url and will attempt to parse the output some number of
    times before failing. meant to address occasional hiccups in service
    which are unaviodable and can be fixed by retrying"""
    try:
        #logger.info('attempting to pull query data')
        url_resp = requests.get(url).content
        parsed_xml = ElementTree.fromstring(url_resp)
        return parsed_xml
    except ElementTree.ParseError:
        if previous_attempts > max_query_attempts:
            return # how do we handle this return
        else:
            query_restful_api(url, previous_attempts + 1)


def xml_to_csv(header_list, csv_writer, xml_object, node_value_fn = lambda x: x):
    # loop for all nodes in the xml
    # for each node use the header list to pull the data in the correct order
    for xml_node in xml_object:
        row_data = [node_value_fn(xml_node.tag) for tag in header_list]
        csv_writer.writerow(row_data)


example_url =  "https://iaspub.epa.gov/enviro/efservice/ENFORCEMENT_ACTION/ROWS/0:10"
example_response = requests.get(example_url)
example_xml = ElementTree.fromstring(example_response.content)
record_xml = example_xml[0]

# make a query for one record and scrape headers from it
header_example_url =  "https://iaspub.epa.gov/enviro/efservice/ENFORCEMENT_ACTION/ROWS/0:0"
header_resp = requests.get(header_example_url)
header_xml = ElementTree.fromstring(header_resp.content)
headers = [node.tag for node in header_xml[0]] # down one level in the tree

base_url = "https://iaspub.epa.gov/enviro/efservice/"
table_name = "ENFORCEMENT_ACTION"
lower_request_bound = 0
records_to_request = 10000

def pull_table(table_name, subdir):
    base_table_url = base_url + table_name + "/ROWS/"

    # single record requested inorder to scrape headers
    header_xml = query_restful_api(base_table_url + "0:0", 10)

    headers = [node.tag for node in header_xml[0]]
    # scrape restful api until complete

    filename = subdir + '/' + table_name + '.tsv'
    os.makedirs(os.path.dirname(filename), exist_ok = True)
    with open(filename, 'w') as filehandle:
        tsv_writer = csv.writer(filehandle, delimiter = '\t') #tab separated value 
        ## we need to be make sure that the files are safe to read in
        ## possibly try to write directly to the excel format?

        # add headers to the csv
        tsv_writer.writerow(headers)
        # currying gives a function what will write the xml to our tsv sheet
        map_xml_to_csv = functools.partial(xml_to_csv,
                                           headers,
                                           tsv_writer,
                                           node_value_fn = lambda str: str.replace('\t', ' '))

        lower_req_bound = 0
        more_data = True
        while more_data:
            upper_req_bound = lower_req_bound + records_to_request
            req_url = base_table_url + str(lower_req_bound) + ':' + str(upper_req_bound)
            logger.info("querying " + req_url)
            # make request
            resp_xml = query_restful_api(req_url, 0)

            # increment the lower bound
            lower_req_bound += records_to_request
            # write data to csv
            map_xml_to_csv(resp_xml)
            # check if there is more data
            if int(resp_xml.attrib['Count']) < records_to_request:
                more_data = False


sdwis_table_reference = [['WATER_SYSTEM_FACILITY', 'SDWIS'],
                         ['TREATMENT', 'SDWIS'],
                         ['LCR_SAMPLE_RESULT', 'SDWIS'],
                         ['VIOLATION', 'SDWIS'],
                         ['ENFORCEMENT_ACTION', 'SDWIS'],
                         ['VIOLATION_ENF_ASSOC', 'SDWIS'],
                         ['GEOGRAPHIC_AREA', 'SDWIS'],
                         ['SERVICE_AREA', 'SDWIS']]


# use list comprehension to call on all the tables


def temp_fn(x):
     pull_table(x[0], x[1])

if __name__ == '__main__':
    p = multi.Pool(processes = 4)
    p.map(temp_fn, sdwis_table_reference)

#[pull_table(*sdwis_table) for sdwis_table in sdwis_table_reference]







