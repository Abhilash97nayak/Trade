from django.shortcuts import render
from rest_framework import serializers,viewsets
from .models import Trade
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
# Create your views here.
fs=FileSystemStorage("tmp")
class TradeSerializer(serializers.ModelSerializer):
   class Meta:
     model= Trade
     fields="__all__"

class Tradeviewset(viewsets.ModelViewSet):
    queryset=Trade.objects.all()
    serializers_class=TradeSerializer  
@csrf_exempt     
@action (detail=False,methods=["POST"])
def upload_data(self,request):
    print("enterinto the ")
    file=request.Files["file"]
    content=file.read()
    #its ain memory file
    #so we need to save the file
    files_saved=ContentFile(content)
    file_named=fs.save("temp.csv",files_saved)
    tmp_file=fs.path(file_named)
    csv_file=open(tmp_file,errors="ignore")
    reader= csv.reader(csv_file)
    candle_detail=[]
    for id_,row in enumerate(reader):
        (
            id,
          date,
          Open,
          close,
          low,
          high,


        )=row
    candle_detail.append(
        Trade(
             id=id,
             date=date,
             open=Open,
             close=close,
             low=low,
             high=high,
        )

    ) 
    Trade.objects.bulk_create(candle_detail)
    return Response("successful")