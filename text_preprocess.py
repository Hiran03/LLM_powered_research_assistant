import pandas as pd
import numpy as np
import re


def preprocessing(filename):
    # Open the file in read mode to read all lines
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    filtered_lines = []
    for line in lines:
        s = line.strip()  # Remove leading/trailing whitespace
        s = re.sub(r'[^\x00-\x7F]', '', s)  # Remove all non-ASCII characters
        s = s.lower()
        s = re.sub(r'\n+', ' ', s)  # Replace multiple newlines with a single space
        # Text cleaning using regular expressions
        s = re.sub(r'\s\W', ' ', s)  # Replace spaces followed by non-word characters
        s = re.sub(r'\W,\s', ' ', s)  # Replace non-word characters followed by commas and spaces
        s = re.sub(r'\s+', ' ', s)  # Replace multiple spaces with a single space
        s = re.sub(r'[!@#$_]', '', s)  # Remove specific special characters (!, @, #, $, _)
        s = s.replace("co", "")  # Remove the substring "co"
        s = s.replace("https", "")  # Remove the substring "https"
        s = s.replace(r"[\w*", " ")  # Remove patterns like "[\w*"
        s = re.sub(r'[^\w\s]', '', s)  # Remove all non-alphanumeric characters except spaces
        
        # Add cleaned line to filtered list if length >= 10
        if len(s) >= 10:
            filtered_lines.append(s + '\n')

    # Open the file in write mode to overwrite with filtered lines
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(filtered_lines)
        
