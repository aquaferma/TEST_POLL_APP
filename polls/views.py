from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from polls import models, serializers
import datetime


class PollsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        # Получение списка активных опросов c вопросами
        polls = models.Poll.objects.filter(date_end__gt=datetime.datetime.now())
        data = serializers.PollSerializer(polls, many=True).data
        return Response(data)


class UserChoiceView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        # Получение списка пройденных опросов с детализацией
        polls = models.Poll.objects.filter(questions__user_choices__user=request.user)
        polls_data = serializers.PollSerializer(polls, many=True).data

        user_choices = models.UserChoice.objects.filter(user=request.user)
        user_choices_data = serializers.UserChoiceSerializer(user_choices, many=True).data

        return Response({"polls": polls_data, "choices": user_choices_data})

    def post(self, request):
        serializer = serializers.UserChoiceSerializer(data=request.data)

        if not serializer.is_valid() or not serializer.questions_is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)