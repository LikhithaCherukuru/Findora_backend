from app.core.database import supabase
from app.core.config import settings


def get_supabase():
    return supabase


def get_settings():
    return settings