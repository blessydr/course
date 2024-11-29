from django.urls import path
from .views import CourseListCreateView,CourseDetails,CourseUpdateDeleteView,RegisterUserView,LoginView,CourseList

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courseslist/', CourseList.as_view(), name='course-list-create'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('coursesdetails/<int:id>/', CourseDetails.as_view(), name='course-details'),
        path('coursesedit/<int:id>/', CourseUpdateDeleteView.as_view(), name='course_detail_api'),  # URL with course id

]
