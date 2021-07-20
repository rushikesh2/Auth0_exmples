import jwt
from functools import wraps
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from auth0authorization.models import UserPrivateData, UserPublicDetails


# from auth0authorization import
# Create your views here.


def get_token_auth_header(request):
    """Obtains the access token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the access token
    Args:
        required_scope (str): The scope required to access the resource
        :param required_scope:
    """

    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            user_email = decoded.get("https://gslab.com/email")
            # print("User Input::", user_email)
            db_email = list(UserPrivateData.objects.values('email'))
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response

        return decorated

    return require_scope


@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    result_data = []
    data = UserPublicDetails.objects.values('shirts', 'trousers', 'shoes')
    for row in data:
        # print(row)
        result_data.append(row)
    result = JsonResponse(data={'Public_Data': result_data}, status=status.HTTP_200_OK, safe=False)
    return result


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})


@api_view(['GET'])
@requires_scope('read:shirts')
def private_scoped(request):
    result_data = []
    user_id = request.META.get('QUERY_STRING')
    parts = user_id.split('=')
    token = parts[1]
    decoded = jwt.decode(token, verify=False)
    user_email = decoded.get("email")
    private_user_data = list(
        UserPrivateData.objects.filter(email=user_email).values('name', 'nickname', 'email', 'data'))
    user_data = private_user_data[0].get('data')

    user_data = user_data.get('shirts')
    del private_user_data[0]['data']
    private_user_data[0]['shirts'] = user_data
    result_data.append(private_user_data[0])

    result = JsonResponse(data=result_data[0], status=status.HTTP_200_OK, safe=False)
    return result


@api_view(['GET'])
@requires_scope('read:trousers')
def private_scoped_trouser(request):
    result_data = []
    user_id = request.META.get('QUERY_STRING')
    parts = user_id.split('=')
    token = parts[1]
    decoded = jwt.decode(token, verify=False)
    user_email = decoded.get("email")
    private_user_data = list(
        UserPrivateData.objects.filter(email=user_email).values('name', 'nickname', 'email', 'data'))
    user_data = private_user_data[0].get('data')
    user_data = user_data.get('trousers')
    del private_user_data[0]['data']
    private_user_data[0]['trousers'] = user_data
    result_data.append(private_user_data[0])

    result = JsonResponse(data=result_data[0], status=status.HTTP_200_OK, safe=False)
    return result


@api_view(['GET'])
@requires_scope('read:shoes')
def private_scoped_shoes(request):
    result_data = []
    user_id = request.META.get('QUERY_STRING')
    parts = user_id.split('=')
    token = parts[1]
    decoded = jwt.decode(token, verify=False)
    user_email = decoded.get("email")
    private_user_data = list(
        UserPrivateData.objects.filter(email=user_email).values('name', 'nickname', 'email', 'data'))
    user_data = private_user_data[0].get('data')
    user_data = user_data.get('shoes')
    del private_user_data[0]['data']
    private_user_data[0]['shoes'] = user_data
    result_data.append(private_user_data[0])

    result = JsonResponse(data=result_data[0], status=status.HTTP_200_OK, safe=False)
    return result


@api_view(['GET'])
@requires_scope('read:collections')
def private_scoped_collections(request):
    result_data = []
    user_id = request.META.get('QUERY_STRING')
    parts = user_id.split('=')
    token = parts[1]
    decoded = jwt.decode(token, verify=False)
    user_email = decoded.get("email")
    private_user_data = list(UserPrivateData.objects.filter(email=user_email).values('name', 'nickname', 'email', 'data'))
    # print(len(private_user_data)) # changes if user not found
    result = JsonResponse(data=private_user_data[0], status=status.HTTP_200_OK, safe=False)
    return result
