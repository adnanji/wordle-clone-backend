from random import randint
from django.shortcuts import render
from django.template import Origin
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from wordle.models import WordleModel
from wordle.serializers import WordleSerializer
from wordle.wordle import WordleStatus

# Create your views here.
class WordleGetApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):

        list_of_pks = WordleModel.objects.values_list('pk', flat=True)

        if not list_of_pks: return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        random_wordle_instance = WordleModel.objects.get(
            pk = list_of_pks[randint(0, len(list_of_pks)-1)]
        )

        random_wordle_instance_ser = WordleSerializer(random_wordle_instance, many=False)

        return Response(random_wordle_instance_ser.data, status=status.HTTP_200_OK)


class WordleCheckApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, guess, wordle_id, tries, *args, **kwargs):

        try:
            orig_wordle = WordleModel.objects.get(pk=wordle_id)
        except WordleModel.DoesNotExist:
            return Response({
                "word": None,
                "gameStatus": WordleStatus.INTERNAL_ERROR
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        if not len(guess) == len(orig_wordle.wordle):
            return Response({
                "word": None,
                "gameStatus": WordleStatus.INCOMPLETE_LETTERS
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        # try:
        #     guessed_wordle = WordleModel.objects.get(wordle=guess)
        # except WordleModel.DoesNotExist:
        #     return Response({
        #         "word": None,
        #         "notification": "This Word Is Not In The List"
        #     }, status=status.HTTP_404_NOT_FOUND)

        
        from .wordle import Wordle

        w = Wordle(original=orig_wordle.wordle, guess=guess, tries=tries)
        
        return Response({
            "word": w.get_wordle(),
            "gameStatus": w.get_status()
        })