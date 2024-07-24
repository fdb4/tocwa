from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Main,Category,Cart,Cartitem
from django.http import FileResponse
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
import io
import itemlistings.serializers as serializers
from .miscfeat import render_to_pdf

# Create your views here.
class itemCreateView(generics.CreateAPIView):
    queryset = Main.objects.all()
    serializer_class = serializers.postItems()
    http_method_names = ['post']

class itemListView(APIView):

    def get(self,request):
        queryset = Main.objects.all()
        serializer = serializers.getItems(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class orderView(APIView):
    def post(self,request):
        serializer= serializers.createOrder(data=request.data)
        if serializer.is_valid():
            serializer.save()#saves to database
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
class orderViewFilterLatest(APIView):
    def get(self,request,name):
        try:
            queryset=Cart.objects.filter(userName=name).latest('LastModified')
            serializer=serializers.OrderFilterLatest(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error": "No items found"}, status=status.HTTP_404_NOT_FOUND)
class orderItems(APIView):
    def post(self,request):
        #data=json.loads(request.data)
        for item in request.data:
            print(item)
            serializer=serializers.cartitems(data=item)
            print(serializer.is_valid())
            if serializer.is_valid() ==False:
                return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            #else:
                #serializer.save()
        #add this to the miscfeat(misc features) file later
        subject1=request.data[0]["cartID"]
        s="order # "+str(subject1)+"has been made"

        m=r"http://127.0.0.1:8000/customer/invoice/"+str(subject1)+"/"
        send_mail(subject=s,message=m,from_email=None,recipient_list=["insertemailhere",])

        return Response(request.data,status=status.HTTP_201_CREATED)
class reciept(APIView):

    def get(self,request,ordernum):
        try:
            id=ordernum
            total=0
            queryset=Cart.objects.filter(cartID=id).latest('LastModified')
            querysetci=Cartitem.objects.filter(cartID=queryset)
            cartstuff=serializers.OrderFilterLatest(queryset)
            cartlist=serializers.recitemcartlist(querysetci,many=True)
            print(cartstuff.data)
            print(cartlist.data)
            for item in cartlist.data:
                print(item["itemID"])
                if item["lbwanted"]==None:
                    total += (item["itemID"]["price"] * item["quantity"])
                else:
                    total+=(item["itemID"]["price"]*item["quantity"]*item["lbwanted"])
            print(total)
            tax=total*.06625
            grandtotal=tax+total
            return render_to_pdf('pdfs/recipt.html', {"cartstuff":cartstuff.data,"cartlist":cartlist.data,"tax":round(tax,2),"total":round(total,2),"grandtotal":round(grandtotal,2)})
        except:
            return Response({"error": "No items found"}, status=status.HTTP_404_NOT_FOUND)

'''
class  categoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.categorySerializer
    http_method_names = ['get']
class createOrderView(generics.ListAPIView):
    queryset = Category.object.all()
    serializer_class = serializers.categorySerializer
    http_method_names = ['post']
'''

