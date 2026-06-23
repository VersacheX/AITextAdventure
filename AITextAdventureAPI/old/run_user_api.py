import os
from dotenv import load_dotenv

# load .env from same directory as this file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

import uvicorn

from user_api.user_api import app

if __name__ == '__main__':
 host = os.environ.get('USER_API_HOST', '127.0.0.1')
 port = int(os.environ.get('USER_API_PORT', '8001'))
 # Disable reload to avoid uvicorn reloader spawning a separate process that triggers startup twice
 uvicorn.run(app, host=host, port=port, reload=False, workers=1)
