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
    pprint(question_type)
    query_set = None
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
        return json_response_true("Fetch all questions successfully!", {
            models.QuestionType.SINGLE:
                serializers.SingleChoiceQuestionSerializer(models.SingleChoiceQuestion.objects.all(), many=True).data,
            models.QuestionType.MULTI:
                serializers.MultiChoiceQuestionSerializer(models.MultiChoiceQuestion.objects.all(), many=True).data,
            models.QuestionType.TRUEORFALSE:
                serializers.TrueOrFalseQuestionSerializer(models.TrueOrFalseQuestion.objects.all(), many=True).data,
            models.QuestionType.TEXT:
                serializers.TrueOrFalseQuestionSerializer(models.TrueOrFalseQuestion.objects.all(), many=True).data,
        })

    def get_serializers(self, questions: list[(str, dict)]):
        sers = []
        for question_type in models.QuestionType:
            pprint(len(questions))
            questions = list(filter(lambda pair: question_type == pair[0], questions))
            questions = list(map(lambda pair: pair[1], questions))
            if question_type == models.QuestionType.SINGLE:
                sers.append(serializers.SingleChoiceQuestionSerializer(data=questions, many=True))
            if question_type == models.QuestionType.MULTI:
                sers.append(serializers.MultiChoiceQuestionSerializer(data=questions, many=True))
            if question_type == models.QuestionType.TRUEORFALSE:
                sers.append(serializers.TrueOrFalseQuestionSerializer(data=questions, many=True))
            if question_type == models.QuestionType.TEXT:
                sers.append(serializers.TextQuestionSerializer(data=questions, many=True))

        return sers

    def post(self, request):
        """Create an array of questions"""
        def get_question(data: dict) -> (str, dict):
            data = dict(**data)
            question_type = None
            if "question_type" in data:
                question_type = data.pop("question_type")
            return question_type, data

        questions: str = request.data.get("questions", None)
        if questions is None:
            return json_response_false("No questions provided!")

        try:
            questions: list = json.loads(questions)
        except Exception as e:
            return json_response_false(f"Paring JSON failed: {str(e)}")

        questions: list = list(map(get_question, questions))
        pprint(questions)
        sers = self.get_serializers(questions)

        try:
            for ser in sers:
                ser.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to create questions", e.args[0])

        for ser in sers:
            ser.save()

        return json_response_true("Create a new question successfully!")

    def put(self, request):
        pass

    def query(self, question_type, question_id):
        if question_type == models.QuestionType.SINGLE:
            return models.SingleChoiceQuestion.objects.filter(id=question_id)
        if question_type == models.QuestionType.MULTI:
            return models.MultiChoiceQuestion.objects.filter(id=question_id)
        if question_type == models.QuestionType.SINGLE:
            return models.SingleChoiceQuestion.objects.filter(id=question_id)
        if question_type == models.QuestionType.SINGLE:
            return models.SingleChoiceQuestion.objects.filter(id=question_id)

    def delete(self, request):
        delete_set_raw = request.data.get('delete_set', None)
        if delete_set_raw is None:
            return json_response_false("No field <delete_set> provided")

        try:
            delete_set = json.loads(delete_set_raw)
        except Exception as e:
            return json_response_false(f"Paring JSON failed: {str(e)}")

        for question_type in models.QuestionType:
            if question_type in delete_set.keys():
                for question_id in delete_set[question_type]:
                    res = self.query(question_type, question_id)
                    if res.exists():
                        res.delete()

        return json_response_true("Deleted questions successfully!")
