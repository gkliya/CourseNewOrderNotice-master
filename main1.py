# -*- coding:utf-8 -*-
# @Time     :2020/10/4 15:35
# @Author     :liyuan
# @File      :main1.py
# @Software  :PyCharm

import  datetime
import re
import conf
import func
import requests

def main():
    # 当前时间
    now = datetime.datetime.now()
    func.log('--'*20)
    func.log(f'[{now:%Y-%m-%d %H:%M:%S}]')
    for platform, order_num_requests in conf.platform_order_num_requests.items():
        platform_last_order_num = func.get_platform_last_order_num(platform)
        platform_order_num = 0
        for order_num_request in order_num_requests:
            try:
                if 'post_query' not in order_num_request:
                    response = requests.get(
                        order_num_request['url'],
                        headers=order_num_request['request_header']
                    )
                else:
                    response = requests.post(
                        order_num_request['url'],
                        headers = order_num_request['request_header'],
                        data=order_num_request['post_query']
                    )
                order_num = re.search(order_num_request['pattern'],response.text).group('order_num')
            except Exception:
                func.send_email(
                    f'[{platform}]获取订单数失败，请及时处理',
                    f'[{platform}]获取订单数失败，请及时处理'
                )
                exit()
            platform_order_num += int(order_num)
        func.record_platform_order_num(platform,platform_order_num)
        func.log(f'[{platform}]总订单数 {platform_order_num} 上次记录总订单数 {platform_last_order_num}')

        if (platform_order_num is not None) and (platform_order_num>platform_last_order_num):
            subject = f'[{platform}]订单增加{platform_order_num - platform_last_order_num}'
            content = f'{platform}总订单数 {platform_order_num}\n上次记录总订单数 {platform_last_order_num}'
            func.send_email(subject, content)
    func.end()


if __name__ == '__main__':
    main()