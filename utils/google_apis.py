import os
import sys
import json
import streamlit as st
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from utils.logger import CustomException, logging

def get_google_calendar_service(client_secrets_file, token_file, SCOPES):
    """Builds and returns an authenticated Google Calendar API service."""

    creds = None

    try:
        # Ensure both files are present (streamlit secrets should create them beforehand)
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
            logging.info("Using existing authorized token file.")

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                logging.info("Credentials refreshed successfully.")
            else:
                # 🚫 This won't work on Streamlit Cloud
                logging.error("Token missing or expired. Cannot authenticate in cloud environment.")
                raise Exception("OAuth flow is not supported in Streamlit Cloud. Please upload a valid token.json.")

        service = build("calendar", "v3", credentials=creds)
        logging.info("Google Calendar service initialized successfully.")
        return service

    except Exception as e:
        logging.error("Unable to build Google Calendar service.")
        raise CustomException(e, sys)
