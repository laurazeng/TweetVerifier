from datetime import datetime
import os
from PIL import Image
import pytesseract
import re

# Replace w/ the location of Tesseract-OCR on your machine.
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

file_dir = os.path.dirname(os.path.realpath('__file__'))
file_path = os.path.join(file_dir, 'testimages/test.jpg')

extracted_text = pytesseract.image_to_string(Image.open(file_path))

def get_screen_name(extracted_text):
    """Return the screen name of the user who created the tweet. 

    Keyword arguments: 
    extracted_text -- the text from running pytesseract on a screenshot of a tweet
    """

    # Brute force and not elegant but efficient -- wanted to do this w/ regex, but I don't think it's possible
    return extracted_text.splitlines()[1] 

def get_tweet_time(extracted_text):
    """Return the time that the tweet was created. 

    Keyword arguments: 
    extracted_text -- the text from running pytesseract on a screenshot of a tweet
    """
    
    #TODO: Make the regex work for non-US locations.
    date_pattern = r'\d+/\d+/\d+, \d+:\d+ from [a-zA-Z]+, [a-zA-Z]+'
    for text in extracted_text.splitlines():
        if re.match(date_pattern, text):
            match = text
    
    time = match.split('from')[0].strip()

    #TODO: Make the datetime aware of time zone.
    location = match.split('from')[1].strip()

    return datetime.strptime(time, '%m/%d/%y, %H:%M')

def get_tweet_status(extracted_text, screen_name, tweet_time):
    """Returns the tweet status. 

    Keyword arguments: 
    extracted_text -- the text from running pytesseract on a screenshot of a tweet
    screen_name -- the screen name of the user who created the tweet
    tweet_time -- the time that the tweet was created
    """

    date_text = tweet_time.strftime('%m/%d/%y, %H:%M').lstrip("0").replace(" 0", " ")
    pattern = '%s(.*)%s' %(screen_name, date_text)
    cleaned_text = extracted_text.replace('\n', ' ')
    result = re.search(pattern, cleaned_text)
    
    return result.group(1).strip()
