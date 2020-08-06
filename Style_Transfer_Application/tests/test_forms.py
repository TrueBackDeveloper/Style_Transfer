from ..forms import image_form
from django.test import TestCase


class ImageFormTest(TestCase):

    def test_image_form_for_not_correct_data(self):
        not_correct_data = open('./Style_Transfer_Application/tests/test_data/test.txt', 'rb')
        form_data = {'img_content': not_correct_data, 'img_style': not_correct_data, }
        form = image_form(data=form_data)
        self.assertFalse(form.is_valid())
