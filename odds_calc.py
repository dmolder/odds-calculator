"""
Main file, import necessary ciphers as needed
"""
import argparse

parser = argparse.ArgumentParser(
    description = 'Provides a variety of tools to assist in calculating probabilities.')
args = parser.parse_args()

ODDS = int(input("Enter odds:"))

def us_odds(odds: int) -> str:
    """
    Returns implied probability for US-style odds
    """
    if odds == 100:
        odds = -100
    return str((-1* (odds)) / (-1 * (odds) + 100)) + "%"
print(us_odds(ODDS))
