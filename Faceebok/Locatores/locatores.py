class LocatorsFb:
    HOME_PAGE_FB = "https://www.facebook.com/login/"
    USERNAME_FIELD = "//input[@id='email']"
    PASSWORD_FIELD = "//input[@id='pass']"
    BTN_LOCATOR = "//button[@id='loginbutton']"
    USERNAME_ERRORMESSAGE_LOCATOR = "//body/div[@id='u_0_0_/b']/div[@id='globalContainer']/div[""@id='content']/div[1]/div[2]/div[" \
                                    "2]/form[1]/div[1]/div[1]/div[2] "
    PASSWORD_ERRORMESSAGE_LOCATOR = "//body/div[@id='u_0_0_/b']/div[@id='globalContainer']/div[""@id='content']/div[" \
                                    "1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2] "

    INVALID_USERNAME_NOTYOU_CSSSELECTOR = "body.fbIndex.UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win.x1-5" \
                                          ".Locale_en_GB.cores-gte4._19_u:nth-child(2) " \
                                          "div._10._9lv3.uiLayer._4-hy._3qw:nth-child(25) div._59s7._9l2g div._4t2a " \
                                          "div:nth-child(1) div._4-i2._pig._9kpl._50f4 div._9kpp:nth-child(6) span._9kpq " \
                                          "> a._39g9 "

    ERROR_MESSAGE_LOCATOR_INVALIDUSERNAME = "body.fbIndex.UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win" \
                                            ".x1-5.Locale_en_GB.cores-gte4._19_u:nth-child(2) " \
                                            "div._10._9lv3.uiLayer._4-hy._3qw:nth-child(27) div._59s7._9l2g " \
                                            "div._4t2a div:nth-child(1) div:nth-child(1) div._4-i2._pig._9kpl._50f4 " \
                                            "> div._9kq2:nth-child(7)"

    ERROR_MESSAGE_INVALIPASSWORD = "body._39il._97vt._97vz._97v-._97v_._97w2._97w0._9ax-._9ax_._9ay1"
    ".UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win.x1-5.Locale_en_GB"
    ".cores-gte4._19_u:nth-child(2) div._li:nth-child(2) "
    "div.uiContextualLayerParent:nth-child(1) div.fb_content.clearfix:nth-child(1) "
    "div._4-u5._30ny div._4-u2._1w1t._4-u8._52jv div.login_form_container "
    "form:nth-child(1) div:nth-child(4) div.clearfix._5466._44mg:nth-child(12) > "
    "div._9ay7:nth-child(2)"


    BOTH_EMPTY_LOCATOR = "b//body/div[@id='u_0_0_Cy']/div[@id='globalContainer']/div[@id='content']/div[1]/div[" \
                         "2]/div[2]/form[1]/div[1]/div[1]/div[2] "

    TEST_INVALID_USER_PASS_ERROR_LOCATOR = "h2"

    ASSERTERROR = "//span[contains(text(),'Welcome to Facebook, Gashu')]"
    NEXT_PAGE = "//div[contains(text(),'Continue as Gashu?')]"

    # ************************************* Forgot password **********************************************

    FORGOT_PASSWORD_LINK = "//body/div[@id='u_0_0_e5']/div[@id='globalContainer']/div[@id='content']/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/a[1]"

    NOT_YOU_LOCATOR = "//a[contains(text(),'Not you?')]"
    ACCOUNT_KEY_LOCATOR = "//input[@id='identify_email']"
    SUBMIT_LOCATOR = "did_submit"
    CLICK_BTN_LOCATR = "//button[@id='did_submit']"
    CON_LOC = "button"
    ENTER_LOC = "//input[@id='recovery_code_entry']"
    CONFIRM_LOC = "//button[contains(text(),'Continue')]"
    INCORRECT_EMAIL_LOC = "//a[contains(text(),'Not you?')]"
    FILL_MAIL_LOC = "//input[@id='identify_email']"

    # ************************************* Register locatores ***************************************

    SIGN_UP_LOCATOR = "//a[contains(text(),'Sign up for Facebook')]"
    NAME_FIELD_LOCATOR = "firstname"
    SURE_NAME_LOCATOR = "lastname"
    EMAIL_PHONE_LOCATOR = "reg_email__"
    CONFRIRMATION_EMAIL_LOCATOR = "reg_email_confirmation__"
    INSERT_PASSWORD_LOCATOR = "//input[@id='password_step_input']"
    SELECT_DATE_LOCAT = "//select[@id='day']"
    MONTH_SELECTOR = "//select[@id='month']"
    YEAR_SELECTOR = "//select[@id='year']"
    GENDER_SELECTOR = "//label[contains(text(),'Male')]"
    SIGN_UP_BUTTON = "button"

    BUTTON_SELECTOR = "button"
    WRONG_EMAIL_SELECT = "div"
    ERROR_MESSAGE_PASSWORD = "h2"
    ERROR_MESSAGE_CODE = "//input[@id='code_in_cliff']"
    SEND_EMAIL_SELECTOR = "//a[contains(text(),'Send Email Again')]"
    ERROR_HANDLING_LOCATOR = "https://m.facebook.com/login/?li=hxT4VrfSuaNNUjFqpzj4N2qC&e=1348029&locale2=en_GB&refsrc=https%3A%2F" \
                             "%2Fm.facebook.com%2Flogin%2F"
    SIGNUP_ERROR_HANDLING = "//a[@id='signup-button']"
    EMAIL_ALREADY_USE = "//a[contains(text(),'Already have an account?')]"
    TEST_ALREADY_NEWACCOUNT = "//a[contains(text(),'Sign up for Facebook')]"

    error_assertion = ""
