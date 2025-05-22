#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:25:33 2024

@author: oujakusui
"""

import openai
import requests


# Set your OpenAI API key here
client = openai.Client(api_key='sk-proj-RCDLLGmg4XSMYnPyB1bKT3BlbkFJaIynLMoijF1iTSg2e9YR')

# Example dictionary of companies and their stock tickers
company_tickers = {
    'Apple Inc.': 'AAPL',
    'Microsoft Corporation': 'MSFT',
    'Tesla, Inc.': 'TSLA',
    # Add more companies and their tickers here
}

def get_company_name(text):
    """Uses OpenAI's API to extract the company name from the text."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Specify the model you want to use
            messages=[{"role": "system", "content": "You are a helpful assistant. Answer the question."},
                      {"role": "user", "content": f"Identify the main company mentioned in this text: {text}"}]
        )
        # The latest message is typically the response from the model
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_ticker_symbol(company_name):
    """Looks up the ticker symbol for the company name."""
    return company_tickers.get(company_name, "Ticker not found")

# Example post
post_text = """
Apple Inc. has recently launched the new iPhone 14, which features significant upgrades
over its predecessor, including a better camera system and longer battery life.
"""

# Extract company name
company_name = get_company_name(post_text)
if company_name:
    print("Company Name:", company_name)
    # Get ticker symbol
    ticker = get_ticker_symbol(company_name)
    print("Ticker Symbol:", ticker)
else:
    print("Company name could not be identified.")
