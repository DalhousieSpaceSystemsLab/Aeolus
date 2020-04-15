CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT("stormeye")

SET( src-files
  "main.c"
)

ADD_EXECUTABLE(${PROJECT_NAME} ${src-files})
