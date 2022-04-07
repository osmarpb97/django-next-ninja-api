from ninja import NinjaAPI
from account.api import router as auth_router

api = NinjaAPI(csrf=True)

api.add_router('/auth', auth_router)