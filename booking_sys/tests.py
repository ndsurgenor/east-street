from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViewsAuthorised(TestCase):
    """
    Tests for booking section views when user is signed in
    """

    def test_bookingsite_signed_in(self):
        """
        Tests that 'New Booking' can be accessed without 403 error
        """
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='goodtest',
            password='test#777',
            is_superuser=True,
        )

        self.client.force_login(user)
        assert user.is_authenticated

        response = self.client.get('/bookingsite/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '403.html')

    def test_bookinglist_signed_in(self):
        """
        Tests that 'Current Bookings' can be accessed without 403 error
        """
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='goodtest',
            password='test#777',
            is_superuser=True,
        )

        self.client.force_login(user)
        assert user.is_authenticated

        response = self.client.get('/bookinglist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '403.html')


class TestViewsUnauthorised(TestCase):
    """
    Tests for booking section views when user is not signed in
    """

    def test_bookingsite_not_signed_in(self):
        """
        Tests that attempting to access 'New Booking' displays 403 Error
        """
        response = self.client.get('/bookingsite/')
        self.assertTemplateUsed(response, '403.html')

    def test_bookinglist_not_signed_in(self):
        """
        Tests that attempting to access 'Current Bookings' displays 403 Error
        """
        response = self.client.get('/bookinglist/')
        self.assertTemplateUsed(response, '403.html')


class TestViewsForbidden(TestCase):

    def test_update_forbidden(self):
        """
        Tests that booking cannot be updated by user who is not the owner
        """
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='badtest',
            password='test#666',
            is_superuser=False,
        )

        self.client.force_login(user)
        assert user.is_authenticated

        response = self.client.get('/90/update')
        self.assertTemplateNotUsed(response, 'bookingform.html')
        self.assertEqual(response.status_code, 301)
    
    def test_delete_forbidden(self):
        """
        Tests that booking cannot be deleted by user who is not the owner
        """
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='badtest',
            password='test#666',
            is_superuser=False,
        )

        self.client.force_login(user)
        assert user.is_authenticated

        response = self.client.get('/90/delete')
        self.assertTemplateNotUsed(response, 'bookingdelete.html')
        self.assertEqual(response.status_code, 301)
