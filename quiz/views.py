from pprint import pprint

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from PetClinicBackend.utils import json_response_false, json_response_true
from . import models, serializers


def question_init(request):
    from yaml import load, FullLoader
    from pathlib import Path

    def load_yaml(yaml_path):
        return load(Path(yaml_path).open('r', encoding='utf-8'), Loader=FullLoader)

    def load_questions(yaml_path):
        dict = load_yaml(yaml_path)
        questions = []
        for disease_type in dict:
            for question in dict[disease_type]:
                questions.append({
                    'disease_type': disease_type,
                    'name': "default",
                    **question
                })
        return questions

    sers = [
        serializers.SingleChoiceQuestionSerializer(data=load_questions('./data/single.yml'), many=True),
        serializers.MultiChoiceQuestionSerializer(data=load_questions('./data/multi.yml'), many=True),
        serializers.TrueOrFalseQuestionSerializer(data=load_questions('./data/tof.yml'), many=True),
    ]

    try:
        for ser in sers:
            ser.is_valid(raise_exception=True)
    except Exception as e:
        pprint(e)
        return json_response_false("Init failed!")

    for ser in sers:
        ser.save()

    return json_response_true("success")


@api_view(['GET'])
def get_single_quiz(request, quiz_id):
    qset = models.Quiz.objects.filter(id=quiz_id)
    if not qset.exists():
        return json_response_false("No such quiz!")
    quiz = qset[0]
    students = User.objects.filter(id__in=quiz.students['list'])
    single = models.SingleChoiceQuestion.objects.filter(id__in=quiz.questions[models.QuestionType.SINGLE])
    multi = models.MultiChoiceQuestion.objects.filter(id__in=quiz.questions[models.QuestionType.MULTI])
    tof = models.TrueOrFalseQuestion.objects.filter(id__in=quiz.questions[models.QuestionType.TRUEORFALSE])
    text = models.TextQuestion.objects.filter(id__in=quiz.questions[models.QuestionType.TEXT])

    student_ser = serializers.StudentSerializer(students, many=True)
    single_ser = serializers.SingleChoiceQuestionSerializer(single, many=True)
    multi_ser = serializers.MultiChoiceQuestionSerializer(multi, many=True)
    tof_ser = serializers.TrueOrFalseQuestionSerializer(tof, many=True)
    text_ser = serializers.TextQuestionSerializer(text, many=True)

    return json_response_true(f"Get the details of quiz {quiz_id} successfully!", {
        "quiz": {
            "id": quiz.id,
            "name": quiz.name,
            "duration": quiz.duration,
            "students": {"list": student_ser.data},
            "questions": {
                models.QuestionType.SINGLE: single_ser.data,
                models.QuestionType.MULTI: multi_ser.data,
                models.QuestionType.TRUEORFALSE: tof_ser.data,
                models.QuestionType.TEXT: text_ser.data,
            }
        }
    })


class QuizAPIView(APIView):

    def get(self, request):
        """Get the quiz list"""
        quizs = models.Quiz.objects.all()
        serializer = serializers.QuizSerializer(quizs, many=True)
        msg = "Fetch all quizs successfully!"
        return json_response_true(msg, {
            "quizs": serializer.data
        })

    def post(self, request):
        """Create a new quiz"""
        serializer = serializers.QuizSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return json_response_false("Failed to create a new quiz", {"err": str(e)})

        serializer.save()
        msg = "Create a new quiz successfully!"
        return json_response_true(msg)

    def put(self, request):
        serializer = serializers.QuizSerializer(data=request.data)
        return json_response_true("Modified successfully!")

    def delete(self, request):
        """Delete a quiz """
        quizs = request.data.get('quizs', None)
        if quizs is not None:
            models.Quiz.objects.filter(id__in=quizs).delete()
        return json_response_true("Deleted successfully!")


@api_view(['GET'])
def get_single_question(request, question_type, question_id):
    if question_type == models.QuestionType.SINGLE:
        query_set = models.SingleChoiceQuestion.objects.filter(id=question_id)
        if not query_set.exists():
            return json_response_false(f"No such single choice question {question_id}")
        return json_response_true("Get single choice question", {
            "question": serializers.SingleChoiceQuestionSerializer(query_set[0]).data
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


# @api_view(['GET'])
# def get_questions_by_keywords(request, keywords):
#     pass
#
#
# @api_view(['GET'])
# def get_questions_by_disease_type(request, disease_type):
#     return json_response_true("Successfully!", {
#         models.QuestionType.SINGLE: [],
#         models.QuestionType.MULTI: [],
#         models.QuestionType.TRUEORFALSE: [],
#         models.QuestionType.TEXT: [],
#     })


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
                serializers.TextQuestionSerializer(text, many=True).data,
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
            return json_response_false("Failed to create questions", {"err": str(e)})

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


@api_view(['GET'])
def get_quiz_result_by_user(request, user_id):
    quiz_results = models.QuizResult.objects.filter(user_id=user_id)
    quiz_result_ser = serializers.QuizResultSerializer(quiz_results, many=True)

    return json_response_true(f'Fetch quiz results of {user_id} successfully!', {
        "quiz_results": quiz_result_ser.data
    })


@api_view(['GET'])
def get_quiz_result_by_quiz(request, quiz_id):
    quiz_results = models.QuizResult.objects.filter(quiz_id=quiz_id)
    quiz_result_ser = serializers.QuizResultSerializer(quiz_results, many=True)

    return json_response_true(f'Fetch quiz results of {quiz_id} successfully!', {
        "quiz_results": quiz_result_ser.data
    })


@api_view(['POST'])
def submit_quiz_result(request):
    quiz_id = request.data.get('quiz_id', None)
    user_id = request.data.get('user_id', None)
    score = request.data.get('score', None)

    quiz = models.Quiz.objects.get(id=quiz_id)
    user = User.objects.get(id=user_id)

    models.QuizResult.objects.create(
        quiz=quiz,
        quiz_name=quiz.name,
        user=user,
        user_name=user.username,
        score=score
    )
    return json_response_true("Submit quiz successfully!")
