import logging
from typing import Dict, Any

# Bot Configuration
BOT_TOKEN = "8702965570:AAH2SlpHbDz6g2I44_52QoLIw9aOGqH96-c"
GROUP_ID = "-1003882662461"
ADMIN_ID = 7831462822

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Product Database
PRODUCTS: Dict[int, Dict[str, Any]] = {
    1: {
        "id": 1,
        "name": "📱 iPhone 14 Pro",
        "price": 999,
        "description": "Latest Apple smartphone with A16 Bionic chip",
        "emoji": "📱"
    },
    2: {
        "id": 2,
        "name": "💻 MacBook Air M2",
        "price": 1199,
        "description": "Lightweight laptop with Apple Silicon M2",
        "emoji": "💻"
    },
    3: {
        "id": 3,
        "name": "🎧 AirPods Pro",
        "price": 249,
        "description": "Premium wireless earbuds with noise cancellation",
        "emoji": "🎧"
    },
    4: {
        "id": 4,
        "name": "⌚ Apple Watch Series 8",
        "price": 399,
        "description": "Advanced health and fitness smartwatch",
        "emoji": "⌚"
    },
    5: {
        "id": 5,
        "name": "📺 iPad Pro 12.9",
        "price": 1099,
        "description": "Powerful tablet for work and creativity",
        "emoji": "📺"
    }
}

# Delivery simulation time (in seconds)
DELIVERY_TIME = 10
