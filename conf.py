import os

# 记录所在目录 Windows和Linux使用不同目录
if os.name == 'nt':
    log_dir = r'C:\Users\zhouhuajian\tmp'
else:
    log_dir = '/tmp'


platform_order_num_requests = {
    '腾讯课堂': [{
        'url': 'http://zhouhuajian.ke.qq.com',
        'request_header': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
        },
        'pattern': r'<span class="js-item-num" data-num="(?P<order_num>\d+)">'
    }],
    '网易云课堂': [{
        'url': 'https://study.163.com/dwr/call/plaincall/PlanNewBean.getPlanCourseDetail.dwr?1600847419879',
        'request_header': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
        },
        'pattern': r';s0.learnerCount=(?P<order_num>\d+);',
        'post_query': {
            'callCount': '1',
            'scriptSessionId': '${scriptSessionId}190',
            'httpSessionId': '2bd4ab424230441e9523ced570b4df8c',
            'c0-scriptName': 'PlanNewBean',
            'c0-methodName': 'getPlanCourseDetail',
            'c0-id': '0',
            'c0-param0': 'string:1210406206',
            'c0-param1': 'number:0',
            'c0-param2': 'null:null',
            'batchId': '1600847419490'
        }
    }, {
        'url': 'https://study.163.com/dwr/call/plaincall/PlanNewBean.getPlanCourseDetail.dwr?1600846712792',
        'request_header': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
        },
        'pattern': r';s0.learnerCount=(?P<order_num>\d+);',
        'post_query': {
            'callCount': '1',
            'scriptSessionId': '${scriptSessionId}190',
            'httpSessionId': '2bd4ab424230441e9523ced570b4df8c',
            'c0-scriptName': 'PlanNewBean',
            'c0-methodName': 'getPlanCourseDetail',
            'c0-id': '0',
            'c0-param0': 'string:1210747815',
            'c0-param1': 'number:0',
            'c0-param2': 'null:null',
            'batchId': '1600846712708'
        }
    }],
    'CSDN学院': [{
        'url': 'https://edu-core-api.csdn.net/mp/lecturer/getEarningsList?type=0&goods_name=&page=1&page_size=100',
        'request_header': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
            'Cookie': r'uuid_tt_dd=10_19464441130-1601193804731-928404; dc_session_id=10_1601193804731.876625; p_uid=U010000; __gads=ID=bc95499ebc8708c3-222278ff1ac40029:T=1602756397:RT=1602756397:S=ALNI_MbQmhTPbwa77QckZTd8D0aLlFLLfA; UserName=weixin_45036829; UserInfo=744b5f3182d043b889ee4ce0beea3351; UserToken=744b5f3182d043b889ee4ce0beea3351; UserNick=weixin_45036829; AU=00C; UN=weixin_45036829; BT=1603335638362; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22weixin_45036829%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19464441130-1601193804731-928404!5744*1*weixin_45036829; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fyzkskaka%252F5n5O4pRs%253Futm_source%253D1598583200%2522%252C%2522announcementCount%2522%253A0%257D; dc_sid=ebd730cd494f2a74b9b0679ca608dc3f; c_segment=4; c_first_ref=www.baidu.com; c_first_page=https%3A//blog.csdn.net/weixin_34200004/article/details/106514206; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1605146020,1605146038,1605146895,1605147641; firstDie=1; c_ref=https%3A//edu.csdn.net/lecturer/5527; log_Id_pv=336; log_Id_view=676; log_Id_click=121; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1605167387; c_page_id=https%3A//mp-edu.csdn.net/reward_management; dc_tos=qjod71'
        },
        'pattern': r'"count":(?P<order_num>\d+),'
    }],
    '51CTO学院': [{
        'url': 'https://edu.51cto.com/center/course/lecturer/course?edunav=',
        'request_header': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
            'Cookie': r'gr_user_id=2cb6661c-37ad-43c5-874d-eac1e5c35a34; Hm_lvt_8c8abdb71d78d33dfdb885e0bc71dae0=1601348267,1601431597,1601442418,1601562702; www51cto=1E5897606223CCBE26678D1618F3D8FEkrUt; pub_wechatopen=aG0wVVNVBlQCBQIIVw; 51ctologToken=14301064d73d804b30e13f60bc5f3e6e; _ga=GA1.2.968147076.1596449964; _ourplusFirstTime=120-8-6-14-39-43; _ourplusReturnTime=120-8-6-14-39-43; _ourplusReturnCount=1; looyu_id=21f780897d1eda91b5cbd9906d0c1bc3_20000923%3A2; zg_a998854cdaa844fa86f3d9b8e98a3c22=%7B%22sid%22%3A%201596695985549%2C%22updated%22%3A%201596696000950%2C%22info%22%3A%201596695985557%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%5C%22%24utm_source%5C%22%3A%20%5C%22baidu%5C%22%2C%5C%22%24utm_medium%5C%22%3A%20%5C%22sem%5C%22%2C%5C%22%24utm_content%5C%22%3A%20%5C%22bj09%5C%22%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fedu.51cto.com%2Fcenter%2Fwejob%2Fpromotion%2Findex%3Futm_platform%3Dpc%26utm_source%3Dbaidu%26utm_medium%3Dsem%26utm_content%3Dbj09%26rtm_plan%3D51CTO%25E5%2593%2581%25E7%2589%258C%25E6%258E%25A8%25E5%25B9%25BF%26rtm_unit%3D%25E6%25A0%25B8%25E5%25BF%2583%26rtm_keyword%3D51CTO%25E5%25AD%25A6%25E9%2599%25A2%26rtm_frd%3Dpinpai%26jzl_kwd%3D172854539007%26jzl_ctv%3D38951156324%26jzl_mtt%3D1%26jzl_adt%3Dcl1%26jzl_ch%3D11%26jzl_act%3D30675461%26jzl_cpg%3D127137117%26jzl_adp%3D4792186630%26jzl_sty%3D0%26jzl_dv%3D1%22%2C%22cuid%22%3A%20%2211370155%22%7D; coursetag2=hascoursetag2; look_course_log=%5B24658%2C25232%2C712%2C19343%2C24253%2C20367%2C23586%2C15139%2C13492%2C16132%5D; Hm_lvt_110fc9b2e1cae4d110b7959ee4f27e3b=1601081762; UM_distinctid=173e2ebdaf83c1-09f666d83c4317-4c302273-e1000-173e2ebdaf927; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211370155%22%2C%22first_id%22%3A%221749eede2e94fb-06cba7a390bcb7-4c3f247a-921600-1749eede2ea7b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22topbar%22%7D%2C%22%24device_id%22%3A%221749eede2e94fb-06cba7a390bcb7-4c3f247a-921600-1749eede2ea7b7%22%7D; pub_sauth3=VlINAVYJAlNUUABXVQRVUQRUU1wFWQdUB1QOCgJTBVMEUgFVUF1TBWxbDlVVUA5QAwVUDFFWVw1WVwcAXAdTBFdTCgQDCAMFUFUHVwdXUFZWPlcOU1BVAQxTAA4; 53revisit=1600845340017; waf_cookie=72897e49-21ef-49ae479c1de338036d72b286f44197702bab; PHPSESSID=k665id8pk297bnq09o0tf0v2n3; _csrf=e64f5d3359b82a13bf2523da1a054c91dd42b9e02f6b970614c301aea5bee0b7a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22%25%C9%CAT%99%E04%07%B4z%26U%CD%97%D3%E0%D7FK9%94%5C%7B7%2F%D8+%0BGc%18%03%22%3B%7D; Hm_lpvt_8c8abdb71d78d33dfdb885e0bc71dae0=1601745685; pub_sauth1=0cXt0qqGPlMCBwUBUgxTPQUFBFVQAwQBW1c; pub_sauth2=497c60aa53ad73579cf78a21e8c40117; pub_cookietime=0; _identity=6d45a7863e4daaf21d257b58e4d2a612a449f8b168f7f9fdbc10eaf7476f61fda%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A20%3A%22%5B1261395%2Ctrue%2C43200%5D%22%3B%7D; BigUser=5d463c8099f682e50cbe7859f2172dfe6442bb6c5c509c671113628721bd1e58a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22BigUser%22%3Bi%3A1%3Bs%3A87%3A%226f82VFQDUwFUVVIGCVUIAQoGBQMAXgBWVFQBAgAGBlMHC1FQXVdSVwddWgALVVVQBlcBBlZTAQZQV1QHVQNUWlA%22%3B%7D; acw_tc=2760825d16017456672323492e75a223ec51e3fcc973500690eae55359dfe6; zg_did=%7B%22did%22%3A%20%22173ad425f4d62-08417aeaeddbe9-4c302273-e1000-173ad425f4f2b9%22%7D; zg_c66b72eff73f441d8513d9e9ce5d966b=%7B%22sid%22%3A%201601745674361%2C%22updated%22%3A%201601745684956%2C%22info%22%3A%201601348267559%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201601745674361%2C%22cuid%22%3A%20%2211370155%22%7D'
        },
        'pattern': r'<p>付费学员: (?P<order_num>\d+)人</p>'
    }],
}

