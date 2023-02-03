from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_202_ACCEPTED
from .serializers import LoginSerializers
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
def login(request):

    # if user request is GET
    if request.method == 'GET':
        data = {'data': 'login'}
        return Response(data)

    # if request is POST
    elif request.method == 'POST':

        # convert data into json format
        serializer = LoginSerializers(data=request.data)

        # validate converted data
        if serializer.is_valid(raise_exception=True):

            # check the data contain user and password
            if serializer.validated_data['user'] == 'aswin' and serializer.validated_data['password'] == '1234':
                # Return Success status
                return Response({'status': 'success'}, status=HTTP_202_ACCEPTED)

            # if user and password is not valid
            else:
                # return status valid user or password
                return Response({'status': 'invalid user or password'}, status=HTTP_404_NOT_FOUND)

        # if data is not in json format
        else:
            # return error
            return Response(serializer.errors)
