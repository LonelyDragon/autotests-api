from __future__ import annotations

from pydantic import BaseModel, Field, ConfigDict


class GetExercisesQuerySchema(BaseModel):
    """Описание структуры запроса на получение списка заданий курса."""
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """Описание структуры запроса на создание заданий курса."""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """Описание структуры ответа при создания задания."""
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """Описание структуры запроса на обновление заданий курса."""
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """Описание структуры ответа при обновлении задания."""
    exercise: ExerciseSchema


class ExerciseSchema(BaseModel):
    """Описание структуры задания."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """Описание структуры ответа получения списка заданий."""
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """Описание структуры ответа полученного задания."""
    exercise: ExerciseSchema
