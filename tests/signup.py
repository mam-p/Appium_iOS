"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import pytest
from appium import webdriver
from time import sleep
from helpers import generate_email

# App pages
import GetStartedPage
import EnterEmailPage
import CreatePasswordPage
import CreateProfilePage
import EnterReferralCodePage
import CustomWelcomePage
import YourPHAPage

class SignUpTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app='/Users/mam-p/Library/Developer/CoreSimulator/Devices/3DBA690A-A052-47FD-94AE-5DD623DA22E7/data/Containers/Bundle/Application/096EA798-2029-4D92-B8F7-8D805EBEE0E4/better-qa.app'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.3',
                'deviceName': 'iPhone 6'
            })
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_signup_group_many_select_service(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info()

        enter_referral_code_page = EnterReferralCodePage.EnterReferralCodePage(self.driver)
        enter_referral_code_page.enter_referral_code('group-many')

        sleep(3) # Simulate user spending a few seconds to read the content on the custom welcome screen
        custom_welcome_page = CustomWelcomePage.CustomWelcomePage(self.driver)
#        assert not(custom_welcome_page.is_default_background_displayed()), 'Default background displayed when custom background should be'
        custom_welcome_page.tap_next()

        your_pha_page = YourPHAPage.YourPHAPage(self.driver)
        your_pha_page.select_service()

        assert not(your_pha_page.is_messaging_tutorial_present()), 'White-on-orange messaging tutorial present after user selected service'
        assert your_pha_page.is_selected_service_message_present(), 'Message related to selected service was not sent/displayed'

    def test_signup_group_one_select_service(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info()

        enter_referral_code_page = EnterReferralCodePage.EnterReferralCodePage(self.driver)
        enter_referral_code_page.enter_referral_code('group-one')

        sleep(3) # Simulate user spending a few seconds to read the content on the custom welcome screen
        custom_welcome_page = CustomWelcomePage.CustomWelcomePage(self.driver)
#        assert not(custom_welcome_page.is_default_background_displayed()), 'Default background displayed when custom background should be'
        custom_welcome_page.tap_next()

        your_pha_page = YourPHAPage.YourPHAPage(self.driver)
        your_pha_page.select_only_service()

        assert not(your_pha_page.is_messaging_tutorial_present()), 'White-on-orange messaging tutorial present after user selected service'
        sleep(30)
        assert your_pha_page.is_selected_service_message_present(), 'Message related to selected service was not sent/displayed'

    def test_signup_group_many_decline_service(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info()

        enter_referral_code_page = EnterReferralCodePage.EnterReferralCodePage(self.driver)
        enter_referral_code_page.enter_referral_code('group-many')

        sleep(3) # Simulate user spending a few seconds to read the content on the custom welcome screen
        custom_welcome_page = CustomWelcomePage.CustomWelcomePage(self.driver)
#        assert not(custom_welcome_page.is_default_background_displayed()), 'Default background displayed when custom background should be'
        custom_welcome_page.tap_next()

        your_pha_page = YourPHAPage.YourPHAPage(self.driver)
        your_pha_page.decline_service()

        assert your_pha_page.is_messaging_tutorial_present(), 'White-on-orange messaging tutorial NOT present after service declined'

    def test_signup_group_with_blank_padded_email(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        email = " " + generate_email() + " "
        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email(email)

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info()

        enter_referral_code_page = EnterReferralCodePage.EnterReferralCodePage(self.driver)
        enter_referral_code_page.enter_referral_code('group-many')

        sleep(3) # Simulate user spending a few seconds to read the content on the custom welcome screen
        custom_welcome_page = CustomWelcomePage.CustomWelcomePage(self.driver)
#        assert not(custom_welcome_page.is_default_background_displayed()), 'Default background displayed when custom background should be'
        custom_welcome_page.tap_next()

        your_pha_page = YourPHAPage.YourPHAPage(self.driver)
        your_pha_page.decline_service()

    def test_signup_group_with_blank_padded_referral_code(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info()

        enter_referral_code_page = EnterReferralCodePage.EnterReferralCodePage(self.driver)
        enter_referral_code_page.enter_referral_code('    group-many ')

        sleep(3) # Simulate user spending a few seconds to read the content on the custom welcome screen
        custom_welcome_page = CustomWelcomePage.CustomWelcomePage(self.driver)
#        assert not(custom_welcome_page.is_default_background_displayed()), 'Default background displayed when custom background should be'
        custom_welcome_page.tap_next()

        your_pha_page = YourPHAPage.YourPHAPage(self.driver)
        your_pha_page.decline_service()

        assert your_pha_page.is_messaging_tutorial_present(), 'White-on-orange messaging tutorial NOT present after service declined'

#####################################################
# NEGATIVE TESTS
#####################################################

    def test_signup_email_missing_extension_neg(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email("test@getbetter")
        assert not(enter_email_page.is_action_button_enabled()), 'Action button enabled despite invalid email address'

    def test_signup_email_with_embedded_blank_neg(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email("test+20150904 144000@getbetter.com")
        assert not(enter_email_page.is_action_button_enabled()), 'Action button enabled despite invalid email address'

    @pytest.mark.current
    def test_signup_email_with_extraneous_at_sign(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email("test+20150904@144000@getbetter.com")
        assert not(enter_email_page.is_action_button_enabled()), 'Action button enabled despite invalid email address'

    def test_signup_missing_first_name_neg(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info(first_name=' ')
        
        assert not(create_profile_page.is_action_button_enabled()), 'Action button enabled despite missing first name'

    def test_signup_password_too_short_neg(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password('qwertyu')

        assert not(create_password_page.is_action_button_enabled()), 'Action button enabled despite too short of password'

    def test_signup_invalid_referral_code_neg(self):
        get_started_page = GetStartedPage.GetStartedPage(self.driver)
        get_started_page.tap_action_button()

        enter_email_page = EnterEmailPage.EnterEmailPage(self.driver)
        enter_email_page.enter_email()

        create_password_page = CreatePasswordPage.CreatePasswordPage(self.driver)
        create_password_page.enter_new_password()

        create_profile_page = CreateProfilePage.CreateProfilePage(self.driver)
        create_profile_page.enter_profile_info()

        enter_referral_code_page = EnterReferralCodePage.EnterReferralCodePage(self.driver)
        enter_referral_code_page.enter_referral_code('nonexistent')
        assert enter_referral_code_page.is_referral_code_invalid_warning_present(), 'No warning about invalid referral code'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
