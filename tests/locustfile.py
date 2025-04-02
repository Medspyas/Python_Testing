from locust import HttpUser, between, task


class test_performance(HttpUser):
    wait_time = between(2, 3)

    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def load_competitions_list(self):
        self.client.get("/")

    @task
    def purchase_place(self):
        self.client.post(
            "/purchasePlaces",
            data={"club": "Simply Lift", "competition": "Fall Classic", "places": "2"},
        )
