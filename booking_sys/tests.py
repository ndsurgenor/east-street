from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def test_update_forbidden(self):
        """
        Tests that booking cannot be updated by user who is not the owner
        """
        user_model = get_user_model()
        bad_username = 'badtest'
        bad_password = 'test#666'
        user = user_model.objects.create_user(
            username=bad_username,
            password=bad_password,
            is_superuser=False,
        )
        signed_in = self.client.login(
            username=bad_username,
            password=bad_password,
        )

        self.assertTrue(signed_in)
        response = self.client.get('/10/update')
        self.assertEqual(response.status_code, 301)
    
    def test_delete_forbidden(self):
        """
        Tests that booking cannot be deleted by user who is not the owner
        """
        user_model = get_user_model()
        bad_username = 'badtest'
        bad_password = 'test#666'
        user = user_model.objects.create_user(
            username=bad_username,
            password=bad_password,
            is_superuser=False,
        )
        signed_in = self.client.login(
            username=bad_username,
            password=bad_password,
        )

        self.assertTrue(signed_in)
        response = self.client.get('/10/delete')
        self.assertEqual(response.status_code, 301)
