from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from jose import jwt
import json
from .models import Book
from .tasks import get_password_hash
import os

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = jwt.encode(
                {'user_id': user.id},
                os.getenv('JWT_SECRET'),
                algorithm='HS256'
            )
            return JsonResponse({'access_token': token})
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def book_list(request):
    if request.method == 'GET':
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authentication required'}, status=401)
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
            books = Book.objects.all().values('title', 'author', 'isbn')
            return JsonResponse(list(books), safe=False)
        except jwt.JWTError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
    return JsonResponse({'error': 'Method not allowed'}, status=405)