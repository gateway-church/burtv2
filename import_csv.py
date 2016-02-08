#!/usr/bin/env python

import os
import sys
import argparse
import pandas as pd
import boto3

def import_csv_to_dynamodb(table_name, csv_file_name, column_names, column_types):
    '''
    Import a CSV file to a DynamoDB table
    '''        

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    items = []

    csv_file = pd.read_csv(csv_file_name, usecols=column_names)
    with table.batch_writer() as batch:
	for i,row in csv_file.iterrows():
	    item = {} 
	    for name in column_names:
		item[name] = str(row[name])
	    batch.put_item(Item=item)
	    print item

def main(prog_args):
    parser = argparse.ArgumentParser(description='Import BURT CSV data to DynamoDB')
    parser.add_argument('csv_file_name')
    args = parser.parse_args()

    column_names = 'domain forward'.split()
    table_name = 'BURT'
    column_types = [str, str]
    import_csv_to_dynamodb(table_name, args.csv_file_name, column_names, column_types)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
