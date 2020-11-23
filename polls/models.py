from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Poll(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название опроса")
    description = models.TextField(verbose_name="Описание")
    date_start = models.DateTimeField(verbose_name="Дата старта")
    date_end = models.DateTimeField(verbose_name="Дата окончания")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")

    class Meta:
        verbose_name = "Тип опроса"
        verbose_name_plural = "Типы опросов"

    def __str__(self):
        return self.name


class Question(models.Model):
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, verbose_name="Тип")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions", verbose_name="Опрос")
    body = models.TextField(verbose_name="Текст вопроса")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.body


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", verbose_name="Вопрос")
    text = models.CharField(max_length=255, verbose_name="Вариант")

    class Meta:
        verbose_name = "Вариант ответа на вопрос"
        verbose_name_plural = "Варианты ответов на вопросы"

    def __str__(self):
        return self.text


class UserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="user_choices", verbose_name="Вопрос")
    answers = models.ManyToManyField(AnswerOption, blank=True, verbose_name="Варианты ответа")
    text = models.TextField(null=True, blank=True, verbose_name="Текстовый вариант ответа")

    class Meta:
        verbose_name = "Вариант ответа пользователя"
        verbose_name_plural = "Варианты ответов пользователей"

    def __str__(self):
        return self.user.username if self.user else "Anonymous"



