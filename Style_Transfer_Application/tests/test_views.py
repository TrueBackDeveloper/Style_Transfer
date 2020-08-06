from django.test import TestCase
from django.urls import reverse


class Show_main_page_tests(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show_main_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Style_Transfer_Application/main_page.html')


class Upload_img_tests(TestCase):

    def test_view_for_correct_data(self):
        img_content = open('./Style_Transfer_Application/tests/test_data/test_1.jpg', 'rb')
        img_style = open('./Style_Transfer_Application/tests/test_data/test_2.png', 'rb')

        response = self.client.post(reverse('Style_Transfer_Application:upload_img', ),
                                    {'img_content': img_content, 'img_style': img_style, })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('show_main_page',))

    def test_view_for_not_correct_data(self):
        not_correct_data = open('./Style_Transfer_Application/tests/test_data/test.txt', 'rb')

        response = self.client.post(reverse('Style_Transfer_Application:upload_img', ),
                                    {'img_content': not_correct_data, 'img_style': not_correct_data, })
        self.assertEqual(response.status_code, 404)

    def test_view_for_not_correct_post_method(self):
        response = self.client.post(reverse('Style_Transfer_Application:upload_img', ))
        self.assertEqual(response.status_code, 404)

