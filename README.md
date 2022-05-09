# Archive Org Batch Link Generator

Archive.org is a treasure chest, but sometimes it is hard to extract the download links in bulk from a search of more than 100 results.

What this code does is using selenium to capture all of the links within a collection, go through each of these links and scrape the url of the file extension (All caps) you specified in the code. The links will then be outputted into an excel spreadsheet that you can just use tools such as JDownloader to download all of the files.

