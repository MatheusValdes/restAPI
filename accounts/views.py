from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework import status, authentication, permissions

from .models import  Condominio, Contatos
from .serializers import CondominioSerializer, ContatosSerializer

from datetime import datetime, timedelta
import os



def teste(request):
    return HttpResponse("Hello World")
#### View para cliente ver qual condominio tem sob seu cadastro

#@api_view(['GET'])
class CondominioAdminListar(ListCreateAPIView):
    ''' Lista todos os condominio, visivel para admin'''
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    permission_classes = [permissions.IsAdminUser]


class Condominios(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the condominios items for given requested user
        '''
        queryset = Condominio.objects.filter(user = request.user.id)
        serializer = CondominioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the condominio with given codominio data
        '''
        serializer = CondominioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CondominioDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk,request):
        try: 
            cond = Condominio.objects.get(pk=pk)
            if cond.user == request.user or request.user.is_staff:
                print("estou aqui")
                return cond
            else: 
                print("permissao negada")
                raise PermissionDenied({"message":"You don't have permission to access",
                                "object_id": cond.id})
        except Condominio.DoesNotExist:
            print("nao existe")
            raise Http404
        except PermissionDenied:
            print("permissao resposta")
            raise PermissionDenied

    def get(self, request,pk, format=None):
        queryset = self.get_object(pk,request)
        serializer = CondominioSerializer(queryset)
        return Response(serializer.data)
    

    def put(self,request,pk,format=None):
        queryset = self.get_object(pk,request)
        serializer = CondominioSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # {
    # "name": "Condominio 2",
    # "phone": 1,
    # "email": "condominio2@akvofluo.com",
    # "num_blocos": 25,
    # "zip_code": "1",
    # "concessionaria": "CAESB",
    # "faixa": "Residencial",
    # "parceiro_set": []
    # }
    
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk,request)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
########################## CONTATO ##################################
    
class ContatosAdminListar(ListCreateAPIView):
    ''' Lista todos os contatos, visivel para admin'''
    queryset = Contatos.objects.all()
    serializer_class = ContatosSerializer
    permission_classes = [permissions.IsAdminUser]

class ContatosList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the contacts items for given requested condominio
        '''
        #print(request.user.codominio)
        queryset = Contatos.objects.filter(cond__user = request.user)
        serializer = ContatosSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the condominio with given codominio data
        '''
        serializer = ContatosSerializer(data=request.data)
        if serializer.is_valid():
            condominio = Condominio.objects.get(user=request.user)
            serializer.save(cond=condominio)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContatosDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk,request):
        try: 
            contato = Contatos.objects.get(pk=pk)
            if contato.cond.user == request.user or request.user.is_staff:
                print("estou aqui")
                return contato
            else: 
                print("permissao negada")
                raise PermissionDenied({"message":"You don't have permission to access",
                                "object_id": contato.id})
        except Contatos.DoesNotExist:
            print("contato nao existe")
            raise Http404
        except PermissionDenied:
            print("permissao resposta")
            raise PermissionDenied

    def get(self, request,pk, format=None):
        queryset = self.get_object(pk,request)
        serializer = ContatosSerializer(queryset)
        return Response(serializer.data)
    

    def put(self,request,pk,format=None):
        queryset = self.get_object(pk,request)
        serializer = ContatosSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk,request)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
class ClienteList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # user = request.user
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente,many=True)
        return Response(serializer.data)




class ClienteCreate(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClienteSerializer
    
#     def create(self,request,*args, **kwargs):
#       usuario = request.user
#        print(usuario)
#        print(self.data)
#        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, 
                        pago=True,
                        pago_em=datetime.today(),
                        valido_ate=datetime.today() + timedelta(days=32),)
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def tarefaCriar(request):
    # tarefa = Trefa.objects.get(id=pk)
    usuario = request.user
    tarefa_post = Tarefa(author=usuario)
    if request.method == "POST":
        serializer = TarefaSerializer(tarefa_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
'''

