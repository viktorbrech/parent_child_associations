This script processes the included csv file line by line, creating a parent-child relationship for each pair of company IDs.

It uses this endpoint: https://legacydocs.hubspot.com/docs/methods/crm-associations/associate-objects

To run the script, create an ".env" text file in the same directory containing one line with your portal Hapikey as follows:

HAPIKEY=**********

Ways to improve this programme:

* Use the batch endpoint instead for greater speed https://legacydocs.hubspot.com/docs/methods/crm-associations/batch-associate-objects
* Use private app authentication for better security https://developers.hubspot.com/changelog/private-apps-are-now-available
* implement proper error handling and retry logic (e.g. possibly by using the HubSpot Python client library instead of requests)
