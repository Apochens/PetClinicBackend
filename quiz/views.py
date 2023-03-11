import json
from pprint import pprint

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_false, json_response_true
from . import models, serializers
from .models import Quiz


@api_view(['GET'])
def get_single_quiz(request, quiz_id):
    qset = Quiz.objects.filter(id=quiz_id)
    if not qset.exists():
        return json_response_false("No such quiz!")
    serializer = serializers.QuizSerializer(qset[0])
    return json_response_true(f"Fetch quiz {quiz_id} successfully", {
        "data": serializer.data
    })


class QuizAPIView(APIView):

    def get(self, request):
        """Get the quiz list"""
        quizs = models.Quiz.objects.all()
        serializer = serializers.QuizSerializer(quizs, many=True)
        msg = "Fetch all quizs successfully!"
        return json_response_true(msg, {
            "list": serializer.data
        })

    def post(self, request):
        """Create a new quiz"""
        serializer = serializers.QuizSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to create a new quiz", e.args[0])

        serializer.save()
        msg = "Create a new quiz successfully!"
        return json_response_true(msg)

    def put(self, request):
        serializer = serializers.QuizSerializer(data=request.data)
        return json_response_true("Modified successfully!")

    def delete(self, request):
        """Delete a quiz """
        quizs = request.data.get('list', None)
        if quizs is not None:

            try:
                quiz_list = json.loads(quizs)
            except Exception as e:
                return json_response_false(r"Parsing JSON failed: {str(e)}")

            for quiz_id in quiz_list:
                if Quiz.objects.filter(id=quiz_id).exists():
                    Quiz.objects.get(pk=quiz_id).delete()
        return json_response_true("Deleted successfully!")


@api_view(['GET'])
def get_single_question(request, question_type, question_id):
    if question_type == models.QuestionType.SINGLE:
        query_set = models.SingleChoiceQuestion.objects.filter(id=question_id)
        if not query_set.exists():
            return json_response_false(f"No such single choice question {question_id}")
        return json_response_true("Get single choice question", {
            "data": serializers.SingleChoiceQuestionSerializer(query_set[0]).data
        })
    if question_type == models.QuestionType.MULTI:
        query_set = models.MultiChoiceQuestion.objects.filter(id=question_id)
        if not query_set.exists():
            return json_response_false(f"No such multi choice question {question_id}")
        return json_response_true("Get multi choice question", {
            "data": serializers.MultiChoiceQuestionSerializer(query_set[0]).data
        })
    if question_type == models.QuestionType.TRUEORFALSE:
        query_set = models.TrueOrFalseQuestion.objects.filter(id=question_id)
        if not query_set.exists():
            return json_response_false(f"No such true or false question {question_id}")
        return json_response_true("Get true or false question", {
            "data": serializers.TrueOrFalseQuestionSerializer(query_set[0]).data
        })
    if question_type == models.QuestionType.TEXT:
        query_set = models.TextQuestion.objects.filter(id=question_id)
        if not query_set.exists():
            return json_response_false(f"No such text question {question_id}")
        return json_response_true("Get text question", {
            "data": serializers.TextQuestionSerializer(query_set[0]).data
        })


class QuestionAPIView(APIView):

    def get(self, request):
        single = models.SingleChoiceQuestion.objects.all()
        multi = models.MultiChoiceQuestion.objects.all()
        tof = models.TrueOrFalseQuestion.objects.all()
        text = models.TrueOrFalseQuestion.objects.all()

        return json_response_true("Fetch all questions successfully!", {
            models.QuestionType.SINGLE:
                serializers.SingleChoiceQuestionSerializer(single, many=True).data,
            models.QuestionType.MULTI:
                serializers.MultiChoiceQuestionSerializer(multi, many=True).data,
            models.QuestionType.TRUEORFALSE:
                serializers.TrueOrFalseQuestionSerializer(tof, many=True).data,
            models.QuestionType.TEXT:
                serializers.TrueOrFalseQuestionSerializer(text, many=True).data,
        })

    def post(self, request):
        """Create an array of questions"""
        sers = []

        single = request.data.get(models.QuestionType.SINGLE, None)
        if single is not None:
            sers.append(serializers.SingleChoiceQuestionSerializer(data=single, many=True))

        multi = request.data.get(models.QuestionType.MULTI, None)
        if multi is not None:
            sers.append(serializers.MultiChoiceQuestionSerializer(data=multi, many=True))

        tof = request.data.get(models.QuestionType.TRUEORFALSE, None)
        if tof is not None:
            sers.append(serializers.TrueOrFalseQuestionSerializer(data=tof, many=True))

        text = request.data.get(models.QuestionType.TEXT, None)
        if text is not None:
            sers.append(serializers.TextQuestionSerializer(data=text, many=True))

        try:
            for ser in sers:
                ser.is_valid(raise_exception=True)
        except Exception as e:
            pprint(e.args)
            return json_response_false("Failed to create questions", e.args[0][0])

        for ser in sers:
            ser.save()

        return json_response_true("Create a new question successfully!")

    def put(self, request):
        pass

    def delete(self, request):

        single = request.data.get(models.QuestionType.SINGLE, None)
        multi = request.data.get(models.QuestionType.MULTI, None)
        tof = request.data.get(models.QuestionType.TRUEORFALSE, None)
        text = request.data.get(models.QuestionType.TEXT, None)

        if single is not None:
            models.SingleChoiceQuestion.objects.filter(id__in=single).delete()
        if multi is not None:
            models.MultiChoiceQuestion.objects.filter(id__in=multi).delete()
        if tof is not None:
            models.TrueOrFalseQuestion.objects.filter(id__in=tof).delete()
        if text is not None:
            models.TextQuestion.objects.filter(id__in=text).delete()

        return json_response_true("Deleted questions successfully!")
