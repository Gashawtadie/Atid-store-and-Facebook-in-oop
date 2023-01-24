class Locatores:
    # ******************store path***************************
    home_path = "https://atid.store/"
    hm_str_pth = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[" \
                 "1]/div[1]/ul[1]/li[2]/a[1] "
    str_pro_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[""1]/ul[1]/li[7]/div[1]/a[1]/img[1]"
    pro_name_path = "//h1[contains(text(),'ATID Yellow Shoes')]"
    str_btn_path = "//button[contains(text(),'Add to cart')]"

    price_str_path = "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[""1]/div[2]/div[2]/p[1]/ins[1]/span[1]/bdi[1]"
    cpn_str_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[""1]/div[1]/div[1]/a[1]"
    store_cpn_field = "//input[@id='coupon_code']"
    store_apply_path = "//button[contains(text(),'Apply coupon')]"
    error_xpath = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[' \
                  '1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1] '

    # ************************ men store**************************************
    # home_path_men = "https://atid.store/"
    hm_men_pth = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[""1]/div[2]/div[1]/div[1]/div[1]/nav[" \
                 "1]/div[1]/ul[1]/li[3]/a[1] "
    men_pro_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[""1]/ul[1]/li[3]/div[1]/a[" \
                   "1]/img[1] "
    pro_name_men_path = "//h1[contains(text(),'ATID Green Tshirt')]"
    men_btn_path = "//button[contains(text(),'Add to cart')]"
    price_men_path = "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[""3]/div[3]/div[1]/div[1]/a[" \
                     "1]/span[1]/span[1]/span[1]/bdi[1] "
    cpn_men_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]"
    men_cpn_field = "//input[@id='coupon_code']"
    men_apply_path = "//button[contains(text(),'Apply coupon')]"

    # ************************* women *************************

    # home_path_wmn = "https://atid.store/"
    hm_wmn_pth = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[""1]/div[2]/div[1]/div[1]/div[1]/nav[" \
                 "1]/div[1]/ul[1]/li[4]/a[1] "
    mwn_pro_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[""1]/ul[1]/li[6]/div[1]/a[1]/img[1]"
    pro_name_path_wmn = "//h1[contains(text(),'Blue Denim Shorts')]"
    str_btn_path_wmn = "//button[contains(text(),'Add to cart')]"
    price_wmn_path = "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[""3]/div[3]/div[1]/div[1]/a[" \
                     "1]/span[1]/span[1]/span[1]/bdi[1] "
    cpn_wmn_crt_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]"
    wmn_cpn_field = "//input[@id='coupon_code']"
    wmn_apply_path = "//button[contains(text(),'Apply coupon')]"

    # ****************************** Accesseries ******************

    # home_path_acc = "https://atid.store/"
    hm_acc_pth = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[""1]/div[2]/div[1]/div[1]/div[1]/nav[" \
                 "1]/div[1]/ul[1]/li[5]/a[1] "
    acc_pro_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[""1]/ul[1]/li[3]/div[1]/a[1]/img[1]"
    pro_name_path_acc = "//h1[contains(text(),'Boho Bangle Bracelet')]"
    str_btn_path_acc = "//button[contains(text(),'Add to cart')]"
    price_acc_path = "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[""1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]/span[""1]/span[1]/span[1]/bdi[1] "
    cpn_acc_crt_path = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[""1]/div[1]/div[1]/a[1]"
    acc_cpn_field = "//input[@id='coupon_code']"
    acc_apply_path = "//button[contains(text(),'Apply coupon')]"

    # ************************************ Search button **********************************

    search_btn_locator = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[" \
                         "3]/div[2]/div[1]/div[1]/a[1]"
    Insert_product_locator = "input"
    search_product_locator = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[" \
                             "1]/div[3]/div[2]/div[1]/div[1]/a[1] "
    check_locator = "//span[contains(text(),'ATID Blue Shoes')]"
    check_results = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/section[1]/h1[1]"
    error_check = "//p[contains(text(),'Sorry, but nothing matched your search terms. Plea')]"
    error_compare = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/section[1]/div[1]"
    positive_pro_name = "//span[contains(text(),'Anchor Bracelet')]"
