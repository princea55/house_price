from django.shortcuts import render
from .apps import PricepredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd
class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            return render(request, 'index.html')

    def post(self, request):
        if request.method == 'POST':
            # get sound from request
            income = request.POST.get('Income')
            age = request.POST.get('Age')
            rooms = request.POST.get('Rooms')
            bedrooms = request.POST.get('Bedrooms')
            population = request.POST.get('Population')
            # np.array([income,age,rooms,bedrooms,population])
            
            price = {'Income': [int(income)],
                'House Age': [int(age)],
                'Number of Rooms': [int(rooms)],
                'Number of Bedrooms': [int(bedrooms)],
                'Area Population': [int(population)]        
                }
            df = pd.DataFrame(price,columns=['Income','House Age','Number of Rooms','Number of Bedrooms','Area Population']) 
            # vectorize sound
            # vector = PricepredictorConfig.vectorizer.transform([income,age,rooms,bedrooms,population])
            # predict based on vector
            prediction = PricepredictorConfig.regressor.predict(df)[0]
            # build response
            response = {'Price': int(prediction)}
            print(prediction)
            # return response
            # return JsonResponse(response)
            return render(request, 'index.html',response)