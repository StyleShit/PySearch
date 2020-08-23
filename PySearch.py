# -*- coding: utf-8 -*-

import requests, re
from urllib import unquote


class PySearch:

    # class constructor
    def __init__( self ):
        # nothing for now
        return


    # search by query and return a list of links by a given count
    def get( self, query, linksCount = 10 ):

        # final links list
        links = []


        # amount of whole pages to extract links from.
        # each page contains 10 links
        wholePagesCount = linksCount / 10

        for i in range( wholePagesCount ):
            links += self.search( query, i * 10 )


        # amount of links to extract from the last page.
        # ( if 'linksCount' doesn't divide by 10 )
        lastPageLinksCount = linksCount % 10

        if lastPageLinksCount != 0:
            links += self.search( query, wholePagesCount, lastPageLinksCount )

        return links


    # fetch google search result by page and links count
    # pages start from 0, and contains 10 results each
    def search( self, query, pageID, count = 10 ):

        # Google search endpoint
        endpoint = "https://www.google.com/search?hl=en&q="  + query + "&start=" + str( pageID )

        # request headers
        headers = {
            "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)",
        }

        # do the search
        res = requests.get( endpoint, headers = headers )
        links = self.extractLinks( res.text )

        # pop links according to the given count ( if needed )
        links = links[:count]

        return links


    # extract links from search results
    def extractLinks( self, searchResults ):

        pattern = r'href="\/url\?q=([^&]+)?'
        matches = re.findall( pattern, searchResults, re.I | re.S )

        if not matches:
            return []

        # remove the last link because it leads to google account page
        matches.pop( -1 )

        return self.urlDecodeMatches( matches )


    # get a list of google search links matches and decode them
    def urlDecodeMatches( self, matches ):
        for i, m in enumerate( matches ):
            matches[i] = unquote( m )

        return matches