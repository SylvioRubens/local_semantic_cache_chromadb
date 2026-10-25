"""Settings for the semantic cache.
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from pathlib import Path

load_dotenv("../.env")

sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = "gemini-3.5-flash-lite"

#The minimum interval between requests to the Gemini API in seconds (The free tier allows 15 requests per minute)
MIN_INTERVAL_S=4.2

#Constants to use as price calculator for price estimation
PRICE_IN_PER_M=0.30
PRICE_OUT_PER_M=2.50

#Threshold for similarity score to consider a cached result as valid
THRESHOLD=0.82

#Time to live for cached results in seconds (default is 100 seconds)
TTL_SECONDS=24*60*60

CACHE_DIR = "../.cache"
COLLECTION_NAME = "semantic_cache"
