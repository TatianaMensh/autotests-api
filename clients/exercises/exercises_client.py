from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание необходимых полей для создания нового задания
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class EditExerciseRequestDict(TypedDict):
    """
    Описание полей для изменения задания
    """
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):

    """
    get_exercises_api – GET /api/v1/exercises. Получение списка заданий для определенного курса.
get_exercise_api – GET /api/v1/exercises/{exercise_id}. Получение информации о задании по exercise_id.
create_exercise_api – POST /api/v1/exercises. Создание задания.
update_exercise_api – PATCH /api/v1/exercises/{exercise_id}. Обновления данных задания.
delete_exercise_api – DELETE /api/v1/exercises/{exercise_id}. Удаление задания.
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий для определенного курса

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.get(url="/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id.
        :param exercise_id: ID задания для получения информации о нем
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.get(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, data: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания нового задания
        :param data: Словарь с данными для создания нового задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.post(url="/api/v1/exercises", json=data)

    def update_exercise_api(self, exercise_id: str, data_update: EditExerciseRequestDict):
        """
        Метод для изменения полей задания
        :param exercise_id: ID задания, которое необходимо изменить
        :param data_update: Словарь с полями для изменения (можно указать только часть)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.patch(url=f"/api/v1/exercises/{exercise_id}", json=data_update)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания по id
        :param exercise_id: ID задания, которое необходимо удалить
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        self.delete(url=f"/api/v1/exercises/{exercise_id}")