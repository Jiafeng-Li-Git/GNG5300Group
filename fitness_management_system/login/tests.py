from django.test import TestCase
import rest_framework
import datetime
from login import models, utils


class TestUtils(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestUtils, cls).setUpClass()
        models.User.objects.create(email='zhouzhouce@gmail.com', password='123456')
        models.Exercise.objects.create(calories=150, duration=10, link="https://www.youtube.com/embed/jWCm9piAwAU")
        d = datetime.date(2022, 10, 19)
        #models.EventData.objects.create(user_id=1, exercise_id=1, exercise_times=1, created_at=d)
        #models.EventData.objects.create(user_id=1, exercise_id=1, exercise_times=2)

    def test_generate_event(self):
        d = datetime.date(2022, 10, 19)
        utils.generate_event_data(1, 1)
        utils.generate_event_data(1, 1)
        event_list = list(models.EventData.objects.all().values())
        assert len(event_list) == 1
        # assert event_list[0]["created_at"] == d
        # assert event_list[1]["created_at"] == datetime.date.today()
        assert event_list[0]["exercise_times"] == 2

    # def test_calculate_calories_duration(self):
    #     res = utils.calculate_calories_duration(1)
    #     assert res == (300, 20)
    #
    # def test_video_details(self):
    #     title = 'HITT'
    #     exercise_obj = models.Exercise.objects.get(exercise_title=title)
    #     exercise_id = exercise_obj.id
    #     utils.generate_event_data(1, exercise_id)
    #     link = exercise_obj.link
    #     assert link == "https://www.youtube.com/embed/jWCm9piAwAU"
