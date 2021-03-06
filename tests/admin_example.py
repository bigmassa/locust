from time import time
from locust import between, HttpLocust, task, TaskSet


class UserBehavior(TaskSet):

    @task(1)
    def admin_index(self):
        self.client.get("/")

    @task(2)
    def list(self):
        self.client.get("/sqlalchemy/demos")

    @task(1)
    def list_search(self):
        self.client.get("/sqlalchemy/demos?search=1")

    @task(1)
    def list_order(self):
        self.client.get("/sqlalchemy/demos?order_by=name&order_direction=asc")

    @task(1)
    def create_get(self):
        self.client.get("/sqlalchemy/demos/create")

    @task(1)
    def create_post(self):
        self.client.post(
            "/sqlalchemy/demos/create",
            data={
                "name": str(int(time())),
                "description": "Description",
                "date": "2021-01-01",
            }
        )

    @task(1)
    def edit_get(self):
        self.client.get("/sqlalchemy/demos/1/edit")

    @task(1)
    def edit_post(self):
        self.client.post(
            "/sqlalchemy/demos/1/edit",
            data={
                "name": str(int(time())),
                "description": "Description",
                "date": "2021-01-01",
            }
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 10)
