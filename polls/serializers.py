from polls import models
from rest_framework import serializers


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionType
        fields = "__all__"


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnswerOption
        exclude = ("question", )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerOptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Question
        exclude = ("poll", )
        depth = 2


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Poll
        fields = "__all__"


class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserChoice
        fields = "__all__"

    def questions_is_valid(self):
        question = self.validated_data.get("question")

        if question.type.id == 1:
            # Ответ текстом
            if not self.validated_data.get("text"):
                return False

        elif question.type.id == 2:
            # Ответ с одним вариантом
            if not len(self.validated_data.get("answers")) != 1:
                return False

        elif question.type.id == 3:
            # Ответ с несколькими вариантами
            if not self.validated_data.get("answers"):
                return False

        return True
