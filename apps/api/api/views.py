from rest_framework import viewsets
from rest_framework import permissions
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    permission_classes = [permissions.AllowAny]
    
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import random
from django.conf import settings

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def generate_mfa_code(request):
    """
    Generates a random MFA code and stores it in the session.
    """
    request.session.modified = True
    mfa_code = str(random.randint(100000, 999999))  # Generate a 6-digit code
    request.session['mfa_code'] = mfa_code
    
    # For testing purposes, you might want to print the MFA code
    if settings.DEBUG:
        print(f"Generated MFA code: {mfa_code}")
    
    return Response({'message': 'MFA code generated successfully.'})

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def validate_mfa_code(request):
    """
    Validates the MFA code submitted by the user.
    """

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def validate_mfa_code(request):
    """
    Validates the MFA code submitted by the user.
    """
    mfa_code = request.data.get('mfa_code')
    user_id = request.data.get('user_id')  # Assuming you have user authentication

    # Retrieve the stored MFA code for the user (e.g., from a database or session)
    stored_mfa_code = request.session.get('mfa_code')

    if not stored_mfa_code:
        return Response({'message': 'MFA code not generated.'}, status=400)

    if mfa_code == stored_mfa_code:
        # Clear the MFA code from the session after successful validation
        del request.session['mfa_code']
        return Response({'message': 'MFA code validated successfully.'})
    else:
        return Response({'message': 'Invalid MFA code.'}, status=400)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def enable_mfa(request):
    user = request.user
    user.mfa_enabled = True
    user.save()
    return Response(status=302)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def mfa_setup(request):
    return Response({'message': 'Choose your MFA method'})

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def disable_mfa(request):
    user = request.user
    user.mfa_enabled = False
    user.save()
    return Response(status=302)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def disable_mfa_confirm(request):
    return Response({'message': 'Confirm Disable MFA'})

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def mfa_recovery(request):
    return Response({'message': 'Account Recovery Instructions'})

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def mfa_recovery_instructions(request):
    return Response({'message': 'Account Recovery Instructions'})

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def enforce_mfa(request):
    return Response(status=302)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def protected_view(request):
    return Response(status=200)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def verify_mfa(request):
    return Response(status=302)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def generate_mfa_secret(request):
    return Response({'message': 'MFA secret generated successfully'})