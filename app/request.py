from app import app
import urllib.request,json
from .models import quotes
Quotes = quotes.Quotes

# Getting the quotes base url
base_url = app.config["QUOTES_API_BASE_URL"]


#Getting Api Key
# api_key = app.config['QUOTES_API_KEY']


def get_quotes():
    """
    function that gets the json response to our url request
    """
    get_quotes_url = base_url.format()
    
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        
        quotes_results = None
        
        if get_quotes_response['results']:
            quotes_results_list = get_quotes_response['results']
            quotes_results = process_results(quotes_results_list)
            
    return quotes_results

def process_results(quotes_list):
    """
    Function that processes the quotes results and transforms them into a list of objects
    
    return:
        quotes_results:a list of quotes
    """
    quotes_results = []
    for quotes_item in quotes_list:
        author = quotes_item.get('author')
        id = quotes_item.get('id')
        quote = quotes.item.get('quote')
        
    return quotes_results