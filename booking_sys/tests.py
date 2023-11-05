from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def test_bookingsite_signed_in(self):
        """
        Tests that the booking form can be accessed when authorised user is signed in
        """
        user_model = get_user_model()
        good_username = 'goodtest'
        good_password = 'test#777'

        user = user_model.objects.create_user(
            username=good_username,
            password=good_password,
            is_superuser=True,
        )
        signed_in = self.client.login(
            username=good_username,
            password=good_password,
        )

        self.assertTrue(signed_in)
        response = self.client.get('/bookingsite/')
        self.assertEqual(response.status_code, 200)


    def test_bookinglist_signed_in(self):
        """
        Tests that previous bookings can be accessed when authorised user is signed in
        """
        user_model = get_user_model()
        good_username = 'goodtest'
        good_password = 'test#777'

        user = user_model.objects.create_user(
            username=good_username,
            password=good_password,
            is_superuser=True,
        )
        signed_in = self.client.login(
            username=good_username,
            password=good_password,
        )

        self.assertTrue(signed_in)
        response = self.client.get('/bookinglist/')
        self.assertEqual(response.status_code, 200)


    def test_bookingsite_not_signed_in(self):
        """
        Tests that the booking form cannot be accessed unless user is signed in
        """
        response = self.client.get('/bookingsite/')
        self.assertEqual(response.status_code, 403)


    def test_bookinglist_not_signed_in(self):
        """
        Tests that a list of bookings cannot be accessed unless user is signed in
        """
        response = self.client.get('/bookinglist/')
        self.assertEqual(response.status_code, 403)


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
        self.assertEqual(response.status_code, 403)
    

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
        self.assertEqual(response.status_code, 403)
