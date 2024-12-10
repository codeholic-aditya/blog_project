# app/middleware/auth_middleware.py
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Check if the user is authenticated by looking for a token in cookies or headers
        token = request.cookies.get("auth_token")  
        print(token)

        # Check if the current route is '/login-page' or '/login', we shouldn't redirect there
        if not token and not request.url.path.startswith("/login"):
            # If token is not found and we are not on the login route, redirect to login
            return RedirectResponse(url="/login-page")

        # Continue with the request if the token is valid or if we're on the login page
        response = await call_next(request)
        return response
