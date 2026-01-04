from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import fake

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="test",
    last_name="test",
    first_name="test",
    middle_name="test"
)
create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print(f"Create file data: {create_file_response}")

create_course_request = CreateCourseRequestSchema(
    title="create_course_request",
    max_score=10,
    min_score=1,
    description="create_course_request",
    estimated_time="1 year",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_response}")

exercise_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestSchema(
    title="create_exercise_request",
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    order_index=1,
    description="create_exercise_request",
    estimated_time="1 year",
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print(f"Create exercise data: {create_exercise_response} ")
