from django.urls import include, path

from .views import classroom, students, teachers_quiz, teachers_course

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('course/', teachers_course.CourseListView.as_view(), name='course_change_list'),
        path('course/add', teachers_course.CourseCreateView.as_view(), name='course_add'),
        path('course/<int:pk>/', teachers_course.CourseUpdateView.as_view(), name='course_change'),

        path('quiz/', teachers_quiz.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teachers_quiz.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers_quiz.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers_quiz.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers_quiz.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', teachers_quiz.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers_quiz.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers_quiz.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),
]
