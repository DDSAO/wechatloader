# This Python file uses the following encoding: utf-8

import tkinter as tk
import os
__author__ = 'ddsao'

class HTMLEditor():
    def __init__(self):
        self._text = ""
        self._location_dict= {}
        self._content = {}

    def find_location(self, text):
        location_list = ['北京','上海','广州','深圳']
        found = False
        current_location = ''

        for location in location_list:
            if found == False and text.find(location) != -1:
                found = True
                current_location = location
            elif found == True and text.find(location) != -1:
                current_location = "多地"
                break

        if found == False:
            return "未知"
        else:
            return current_location

    def add_location_dict(self, text):
        location = self.find_location(text)
        if location in self._location_dict.keys():
            self._location_dict[location].append(text)
        else:
            self._location_dict[location] = [text]

    def get_dict(self):
        return self._location_dict

    def encode(self):
        content = '<section style="box-sizing: border-box;"><section style="opacity: 0.78;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: 15%;box-sizing: border-box;"><section style="box-sizing: border-box;"><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 70%;box-sizing: border-box;"><img class=" __bg_gif" data-ratio="1" data-src="https://mmbiz.qpic.cn/mmbiz_gif/KqlY2OZFQJqL1PtBE5SbsicxYU5yblko9Saiadh2wIbDyARrVVTSILEQkYZJYEBE1yJEYOOaMnzuLldagmtNibqZA/640?wx_fmt=gif" data-type="gif" data-w="260" style="vertical-align: middle; box-sizing: border-box; width: 100% !important; height: auto !important; visibility: visible !important;" _width="100%" src="https://mmbiz.qpic.cn/mmbiz_gif/KqlY2OZFQJqL1PtBE5SbsicxYU5yblko9Saiadh2wIbDyARrVVTSILEQkYZJYEBE1yJEYOOaMnzuLldagmtNibqZA/640?wx_fmt=gif&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1" data-order="0" data-fail="0"></section></section></section></section><section style="display: inline-block;vertical-align: middle;width: 85%;padding-left: 10px;box-sizing: border-box;"><section style="box-sizing: border-box;"><section style="margin-top: 10px;margin-right: 0%;margin-left: 0%;box-sizing: border-box;"><section style="text-align: center;font-size: 13px;color: rgba(16, 16, 16, 0.83);box-sizing: border-box;"><p style="text-align: left;box-sizing: border-box;"><strong style="box-sizing: border-box;">关注并标星“今日实习”</strong></p><p style="text-align: left;box-sizing: border-box;"><strong style="box-sizing: border-box;">第一时间获得<span style="color: rgba(3, 72, 143, 0.933);box-sizing: border-box;">最新实习资讯</span></strong></p></section></section></section></section></section></section>';
        content += '<section style="margin: 10px 0%;box-sizing: border-box;"><section style="display: inline-block;width: 100%;vertical-align: top;background-position: 0% 0%;background-repeat: repeat;background-size: 68.3688%;background-attachment: scroll;padding: 15px;box-shadow: rgb(0, 0, 0) 0px 0px 0px;background-image: url(&quot;https://mmbiz.qpic.cn/mmbiz_png/KqlY2OZFQJq9LBwdkWQSffCdjPsiavCBEYjibtviaZsOhYCk0c7arXCIe1wZL7nnRHfWg1FAoiaL6EzJXHm137LfbQ/640?wx_fmt=png&quot;);box-sizing: border-box;"><section style="box-sizing: border-box;" powered-by="xiumi.us"><section style="box-sizing: border-box;"><section style="font-size: 14px;line-height: 1.5;letter-spacing: 0.3px;padding-right: 8px;padding-left: 8px;box-sizing: border-box;"><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><span style="letter-spacing: 0.3px;box-sizing: border-box;">温馨建议大家在投简历和面试前，一定要记得来回顾我们为大家推出的干货帖：</span><br style="box-sizing: border-box;"></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247483909&amp;idx=1&amp;sn=9535e24f917afc626f50e5ab60e96dfc&amp;chksm=e9faddebde8d54fd2fedfbc89d8b717ba03bbef2d5a19972ae1d8926dc151a1faf5fbb86d127&amp;scene=21#wechat_redirect" data-linktype="2" style="text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">看完后90%的问题可以解决的简历攻略</a></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484199&amp;idx=1&amp;sn=751194c16a4e0ec98bbed97c46633cd0&amp;chksm=e9fadcc9de8d55df4b689eb658dcdf1200c81fad007dd1e92a6e9bb565d95aab4641da2303d1&amp;scene=21#wechat_redirect" data-linktype="2" style="text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">准顶级咨询顾问教大家如何讲述过往经历</a></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484066&amp;idx=1&amp;sn=27b58c68fcf10b8d5d74a142f0439f02&amp;chksm=e9fadd4cde8d545a8d983149918d3be4f6b0ce4004d604b863e36659249b19baab3b9668f8f7&amp;scene=21#wechat_redirect" data-linktype="2" style="text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">群面全过的网易产品经理的群面攻略</a></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br style="box-sizing: border-box;"></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;">此外，我们需要郑重声明：</p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;">本平台所有实习来自用人单位直接发布及网络渠道，小编每天都会优先放送企业邮箱的实习，对于非企业邮箱的实习，若为用人单位主动发布，小编会在用人单位提供名片或工牌后才予以发布；对于来自网络渠道的实习，小编会通过搜索引擎为大家确认是否为明显的营销号或骗子邮箱，以增强实习信息的真实性与可靠性，但由于信息量过大，小编无法保证每条实习的准确性与及时性，还请大家<span style="color: rgb(0, 51, 153);box-sizing: border-box;"><strong style="box-sizing: border-box;">对于非企业邮箱的实习谨慎投递</strong></span>。</p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br style="box-sizing: border-box;"></p><p style="padding-right: 0em;padding-left: 0em;font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><span style="letter-spacing: 0.3px;box-sizing: border-box;">另外，今日实习版权保卫战持续进行中，欢迎各位多多举报抄袭今日实习原创文与实习的行文。</span><span style="letter-spacing: 0.3px;max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">各位火眼金睛的IT粉如果发现抄袭小编为大家整理的实习帖、将今日实习原创文洗稿的公众号<span style="max-width: 100%;letter-spacing: 0.3px;box-sizing: border-box;">或个人</span>，</span><strong style="letter-spacing: 0.3px;max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;color: rgb(0, 51, 153);box-sizing: border-box;overflow-wrap: break-word !important;">欢迎来后台举报，小编将奉上价值99¥的求职大礼包作为奖励。</span></strong></p></section></section></section></section></section>'
        content += self.generate_table()

        for location in self._location_dict.keys():
            content += self.generate_section(self._location_dict.get(location,""),location) +'<p></p>'

        content += self.add_footer()
        return content

    def generate_table(self):
        content=""
        preformat = '<table width=100% style = "border-collapse:collapse;margin:30px 0;">' +\
            '<tr style="text-align: center;border-collapse:collapse">' +\
                '<th width=30% height=40px style = "color:white;background-color:#003399;border:1px solid #003399;">地区</th>' +\
                '<th width=%70 height=40px style = "color:white;background-color:#003399;border:1px solid #003399;">公司</th></tr>'
        postformat = '</table><p style="white-space:normal"></p>'
        for location in self._location_dict.keys():
            content += '<tr>' +\
            '<td height=40px style = "box-sizing:border-box;text-align:center;border:1px solid lightblue">' +\
            location + '*' + str(len(self._location_dict[location])) + '</td>' +\
            '<td height=40px style="box-sizing:border-box;text-align: left; padding-left:5px;border:1px solid lightblue">' +\
            self.get_company_name(self._location_dict[location]) + '</td></tr>'
        return preformat + content + postformat

    def get_company_name(self, list):
        name = ""
        for i, text in enumerate(list):
            if i != len(list)-1:
                name += text.split('\n',1)[0] + ', '
            else:
                name += text.split('\n',1)[0]
        return name

    def generate_section(self, list,location):
        content=''
        '''
        <section>
            <section>
                <span><p><strong>the label</strong></p></span>
            <section>
            <section>
                <section>
                    <p>article</p>
                </section>
            <section>
        </section>
        '''
        preformat = '<section style="margin-top: 10px;margin-bottom: 10px;text-align: center;box-sizing: border-box;">' +\
        '<section style="padding-left: 1em;padding-right: 1em;display: inline-block;box-sizing: border-box;">'+\
        '<span style="display: inline-block;padding: 0.3em 0.5em;box-shadow: #A5A5A5 4px 4px 2px;background-color: rgba(10, 82, 180, 0.9);font-size: 15px;color: #FFFFFF;box-sizing: border-box;"><p style="box-sizing: border-box;">' +\
            '<strong>' + location + '*' + str(len(list)) + '</strong></p></span></section>' + \
        '<section style = "border-width: 1px;border-style: solid;border-color: rgb(204, 204, 204);margin-top: -1em;box-shadow: rgb(165, 165, 165) 4.2px 4.2px 2px;padding: 20px 10px 10px;background-color: rgb(255, 255, 255);box-sizing: border-box;" >' +\
        '<section style = "text-align: left;font-size: 14px;line-height: 1.5;padding-right: 8px;padding-left: 8px;letter-spacing: 0.3px;box-sizing: border-box;" >'
        postformat = '</section></section></section>'
        for text in list:
            content += self.add_p(text) + '<br>'
        return preformat + content + postformat

    def add_p(self,text):
        text_list = text.split('\n');
        content = ''
        for paragraph in text_list:
            content += '<p>' + paragraph + '</p>'
        return content

    def add_footer(self):
        footer1 = '<section style="margin: 10px 0%;box-sizing: border-box;"><section style="display: inline-block;width: 100%;vertical-align: top;background-position: 0% 0%;background-repeat: repeat;background-size: 68.3688%;background-attachment: scroll;padding: 15px;box-shadow: rgb(0, 0, 0) 0px 0px 0px;background-image: url(&quot;https://mmbiz.qpic.cn/mmbiz_png/KqlY2OZFQJq9LBwdkWQSffCdjPsiavCBEYjibtviaZsOhYCk0c7arXCIe1wZL7nnRHfWg1FAoiaL6EzJXHm137LfbQ/640?wx_fmt=png&quot;);box-sizing: border-box;"><section style="box-sizing: border-box;" powered-by="xiumi.us"><section style="box-sizing: border-box;"><section style="font-size: 14px;line-height: 1.5;letter-spacing: 0.3px;padding-right: 8px;padding-left: 8px;box-sizing: border-box;"><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><span style="letter-spacing: 0.3px;">最后，小编要郑重声明：本平台所有实习为免费实习，杜绝一切以此营利的行为，如遇从本平台获取信息并作为付费实习的情况，欢迎IT粉们及时举报。</span><br></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><span style="letter-spacing: 0.3px;box-sizing: border-box;">若在求职过程中遇到收取费用，实习地址、联系方式与平台发布信息不一致的情况，也请提高警惕，并与本平台联系。</span><br style="box-sizing: border-box;"></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;">对本平台内推来源有疑问的同学可戳今日实习<a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484224&amp;idx=1&amp;sn=b99410f307710ffed96407f6f82567f3&amp;chksm=e9fadcaede8d55b81d631e3250dfeef34f1edcb085938a51636eb3b951546ad643a2c01f6b00&amp;scene=21#wechat_redirect" data-linktype="2" style="text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">关于内推的严正声明</a>获得更多详情。</p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><span style="max-width: 100%;letter-spacing: 0.3px;box-sizing: border-box;overflow-wrap: break-word !important;">所有实习信息为小编辛勤整理的结果，未经许可不得转载，</span>转载请联系</p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><strong style="letter-spacing: 0.3px;max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;letter-spacing: 0.3px;color: rgb(0, 51, 153);box-sizing: border-box;overflow-wrap: break-word !important;">internshiptoday@126.com</span></strong></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;"><br></p><p class="" style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;"><span style="max-width: 100%;font-size: 13px;letter-spacing: 0.3px;box-sizing: border-box;overflow-wrap: break-word !important;">/你可能还想看/</span></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247488732&amp;idx=1&amp;sn=e88a460dfd906e48a18ce6ae13765e7d&amp;chksm=e9facb32de8d42248d8319849a4bbe9edcf97ad217f0821f24a3cb9fba6ba7824a2d310ca65e&amp;scene=21#wechat_redirect" target="_blank" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">尝试过FA私募等的我为什么选择投研</span></a></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247488970&amp;idx=1&amp;sn=1ac0cced7afd92ce7da4833b244cca12&amp;chksm=e9faca24de8d43329737cc0bf6459603549b968500023b4b2c5c551f9623e39f194363e88cac&amp;scene=21#wechat_redirect" target="_blank" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);letter-spacing: 0.3px;max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">海外党如何逆袭世界五百强管培生</span></a></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247490320&amp;idx=1&amp;sn=54f81a5147f6edd0519074c25a205401&amp;scene=21#wechat_redirect" target="_blank" data-linktype="2"><span style="color: rgb(51, 102, 153);"><span style="font-size: 12px;"><span style="text-decoration: underline;">非清北复交如何拿到MBB全职offe</span></span></span></a><span style="color: rgb(51, 102, 153);"><span style="font-size: 12px;"><span style="text-decoration: underline;">r</span></span></span></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247491849&amp;idx=1&amp;sn=b45bff4de7685fac80ad3f71f2ede818&amp;scene=21#wechat_redirect" target="_blank" data-linktype="2"><span style="color: rgb(51, 102, 153);"><span style="font-size: 12px;"><span style="text-decoration: underline;">宝洁校招闯关秘籍</span></span></span></a></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484988&amp;idx=1&amp;sn=b2291c77e47fc2f5d1a934e0e4c8aef0&amp;chksm=e9fad9d2de8d50c4148ac2d281d23ef733467475fb3448af7eb06f55441b3742e3754675f7bc&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;' +\
                 'box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">德勤俱乐部</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;|&nbsp;<a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247488462&amp;idx=1&amp;sn=c3f79a48cc6bf7d38a9b6d0cabd46d15&amp;chksm=e9facc20de8d453668749fe27c3667f348a0d37be8e0e057dce02adf342bbb0c017fb376227e&amp;scene=21#wechat_redirect" data-linktype="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">第一份实习</a>&nbsp;|&nbsp;</span><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485343&amp;idx=1&amp;sn=54dc7bfb3228c347a1fefb9b55fe7ef0&amp;chksm=e9fad871de8d5167bb6334ef5ee200906892c2a774e2782733c4e6000ca0578533d787b03dd6&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">实习留用</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;</span></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">北大光华保研分享 |&nbsp;</span><span style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484828&amp;idx=1&amp;sn=9184b2c53338bdaa70257cc8648e575e&amp;chksm=e9fada72de8d5364450729fdd91040cfc21ff59e728b78f1db728353e29d6f24bf34d1b9b5ef&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">腾讯校招产品offer</a></span></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><span style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247489184&amp;idx=1&amp;sn=ad35c56133e2bf526284564f5cf3a4ef&amp;chksm=e9fac94ede8d40581a1b270ee1225040b48237a947e0b25722e5b6bfb9366f1861edeb888733&amp;scene=21#wechat_redirect" target="_blank" data-linktype="2" style="color: rgb(51, 102, 153);letter-spacing: 0.3px;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;letter-spacing: 0.3px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="letter-spacing: 0.3px;">巨头联合试水泛娱乐 |&nbsp;</span></span></a><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247489673&amp;idx=2&amp;sn=b15ef0ca8505e76f6f66c69b9c2d754d&amp;scene=21#wechat_redirect" target="_blank" data-linktype="2" style="letter-spacing: 0.3px;">中国星巴克的转型尝试</a></span></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484811&amp;idx=1&amp;sn=2612891c45173dffb35210f37414a0a6&amp;chksm=e9fada65de8d53735b05134afbb9b86a1fdf86e97f2158daf40ac224d415edafbc33ffe3da01&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">抖音何去何从</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;|&nbsp;</span><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485670&amp;idx=1&amp;sn=b6a6a1e9ffaf8e8a4b162a4f91670598&amp;chksm=e9fad708de8d5e1ecfa51939cfbe6938192101f6049ac62b940369f4f5076caab26d8af5156c&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">美团滴滴之争&nbsp;</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">|</span><a href="http://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247486685&amp;idx=1&amp;sn=5772182a6cc7dc92dd0fa9e4e6b76fb9&amp;chksm=e9fad333de8d5a25aa7ac0b858bd0596dfd0f15cfd8deef24a558ce00055fadc9d58c106db87&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;内容电商变现</span></a><br style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;"></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485203&amp;idx=1&amp;sn=9a5903382b71393dffa08bf0a881480d&amp;chksm=e9fad8fdde8d51eb515acba77751d9' +\
                 '0a5c1e80ccbbe21f16910262d21bbf278febe3aaa97806&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">“苏宁极物”进军线下零售</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;|&nbsp;</span><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485451&amp;idx=1&amp;sn=d0b1d82eab70f612c50a9abb9ad9dbd9&amp;chksm=e9fad7e5de8d5ef38a47a8316f92f1429a30327fe8628efb34215dda09d32dfa6800dd22b5e0&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">网易严选</span></a></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247484918&amp;idx=1&amp;sn=6a0b2099effcc446ee8a8e4fdd90f7eb&amp;chksm=e9fada18de8d530e7150ab090cf5a67d1cbd1a473a59c6c20a4ae47e7dd873eb657c60f03e09&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">树洞001</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;|&nbsp;</span><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485157&amp;idx=1&amp;sn=716a710ad8db386fc4bc0bfb229033ec&amp;chksm=e9fad90bde8d501db425484930843e5950c967840ee77731341100cd1568ae3a763b6d6f4843&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">树洞002 |</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">&nbsp;</span><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485280&amp;idx=1&amp;sn=ebd6de3d4a8eb515466ce2e028ee6d31&amp;chksm=e9fad88ede8d51983789063fd05fde3a8a3977f894779789d1aab74fc98bd180a762685bdc40&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">树洞003&nbsp;</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">|&nbsp;</span><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485415&amp;idx=1&amp;sn=6f8e8b3d4cba12f52b91bcc216077f2e&amp;chksm=e9fad809de8d511f0fd1ad8fe136156a97a008a9788afdfe27c77a746bfb5a6391adb8f3bd39&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">树洞004</span></a></p><p style="font-size: 14px;letter-spacing: 0.3px;white-space: normal;text-align: center;line-height: 1.5em;"><a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485526&amp;idx=1&amp;sn=9edc5a99990c4dc93b936ea30fe7feac&amp;chksm=e9fad7b8de8d5eae99aeb639f3746fa5a32bd37dc910cab22b777c3d362ca0b558a8849d082c&amp;scene=21#wechat_redirect" data-linktype="2" style="color: rgb(51, 102, 153);text-decoration: underline;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">树洞005&nbsp;</span></a><span style="max-width: 100%;text-decoration: underline;color: rgb(51, 102, 153);font-size: 12px;box-sizing: border-box;overflow-wrap: break-word !important;">|&nbsp;<a href="https://mp.weixin.qq.com/s?__biz=MzI1MDg3NDQ5Nw==&amp;mid=2247485640&amp;idx=1&amp;sn=a5fa0c642c9c4d6c1bed13e1fafa5e5b&amp;chksm=e9fad726de8d5e3090aa6544d54d5a94d25a727044631b3380ea736b1ddea32dac044de12781&amp;scene=21#wechat_redirect" data-linktype="2" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">树洞006</a></span></p></section></section></section></section></section>'
        footer2 = '<section style="margin-top: 0.5em;margin-bottom: 0.5em;text-align: center;box-sizing: border-box;"><section style="border-width: 1px;border-style: solid;border-color: rgb(204, 204, 204);box-shadow: rgb(204, 204, 204) 1px 1px 5px;display: inline-block;width: 100%;box-sizing: border-box;"><section style="max-width: 100%;display: inline-block;line-height: 0;box-shadow: rgb(0, 0, 0) 0px 0px 0px;box-sizing: border-box;"><img class="" data-ratio="1" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/KqlY2OZFQJq9LBwdkWQSffCdjPsiavCBECvicGljVgpg5iaCiccia2H2zf5pwLeaayckIkqUbxia8iaCjny6Ziay2CyZiag/640?wx_fmt=jpeg" data-type="jpeg" data-w="430" style="vertical-align: middle; box-sizing: border-box; width: 430px !important; height: auto !important; visibility: visible !important;" _width="430px" src="https://mmbiz.qpic.cn/mmbiz_jpg/KqlY2OZFQJq9LBwdkWQSffCdjPsiavCBECvicGljVgpg5iaCiccia2H2zf5pwLeaayckIkqUbxia8iaCjny6Ziay2CyZiag/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1" crossorigin="anonymous" data-fail="0"></section><section style="width: 100%;height: 1em;margin-top: -0.92em;box-sizing: border-box;"><section style="width: 45%;height: 1em;display: inline-block;vertical-align: top;background-color: rgb(255, 255, 255);box-sizing: border-box;"></section><section style="width: 0px;margin: auto;display: inline-block;vertical-align: top;border-left: 0.8em solid rgb(255, 255, 255);border-right: 0.8em solid rgb(255, 255, 255);border-bottom: 0.8em solid white;border-top: 0.55em solid transparent !important;box-sizing: border-box;"></section><section style="width: 45%;height: 1em;display: inline-block;vertical-align: top;background-color: rgb(255, 255, 255);box-sizing: border-box;"></section></section><section style="width: 100%;margin-top: -1em;box-sizing: border-box;"><section style="width: 10%;height: 1em;display: inline-block;vertical-align: top;background-color: rgb(255, 255, 255);box-sizing: border-box;"></section><section style="width: 10%;height: 1em;margin-left: 80%;display: inline-block;vertical-align: top;background-color: rgb(255, 255, 255);box-sizing: border-box;"></section></section><section style="margin-top: -0.6em;padding: 10px;box-sizing: border-box;"><section style="box-sizing: border-box;" powered-by="xiumi.us"><section style="box-sizing: border-box;"><section style="font-size: 19px;line-height: 1;box-sizing: border-box;"><p style="text-align: left;box-sizing: border-box;"><span style="font-size: 14px;box-sizing: border-box;">【今日实习】是曾在麦肯锡罗兰贝格和埃森哲实习的咨询老司机和前腾讯招聘HR一起创办的求职和申研等背景提升平台，每天搬运海量top实习还有各种独家求职申研干货。<br style="box-sizing: border-box;"></span></p><p style="box-sizing: border-box;"><br style="box-sizing: border-box;"></p><p style="text-align: left;box-sizing: border-box;"><span style="font-size: 14px;box-sizing: border-box;">扫描上方二维码解锁更多精彩，敬请期待下期简历修改、模拟面试、优质活动推荐等服务！如果通过我们平台找到了实习不要忘记来后台报喜噢！</span></p><p style="box-sizing: border-box;"><br style="box-sizing: border-box;"></p><p style="text-align: left;box-sizing: border-box;"><span style="font-size: 14px;box-sizing: border-box;">转载、岗位发布请邮件Internshiptoday@126.com。</span></p></section></section></section></section></section></section>'
        footer3 = '<section style="box-sizing: border-box;"><section style="text-align: right;font-size: 14px;box-sizing: border-box;"><p style="box-sizing: border-box;"><strong style="font-size: 14px;text-align: right;white-space: normal;max-width: 100%;box-sizing: border-box;"><span style="max-width: 100%;box-sizing: border-box;color: rgba(31, 29, 29, 0.65);overflow-wrap: break-word !important;"><strong style="max-width: 100%;box-sizing: border-box;"><span style="max-width: 100%;box-sizing: border-box;overflow-wrap: break-word !important;">点“在看”给小编加鸡腿<span style="max-width: 100%;box-sizing: border-box;color: rgb(51, 51, 51);overflow-wrap: break-word !important;">👇</span></span></strong></span></strong></p></section></section>'
        return footer1 + footer2 + footer3
class APP():
    def __init__(self,root):
        self._root = root
        self._root.title("今日实习编辑器")
        self._editor = HTMLEditor()
        self._record_num = 0

        tk.Label(self._root, text="将一段实习内容粘贴至下方，点击添加").pack()
        self._e = tk.Entry(self._root)
        self._e.focus()
        self._e.pack()

        self._option_f = tk.Frame(self._root)
        self._option_f.pack()

        tk.Button(self._option_f, text="添加",command=self.add_to_editor).pack(side=tk.LEFT)
        tk.Button(self._option_f, text="查看表格", command = self.see_record).pack(side=tk.LEFT)
        tk.Button(self._option_f, text="获取神秘代码", command=self.generate_html).pack(side=tk.LEFT)

        self._record_l = tk.Label(self._root, text="当前录入总数: 0")
        self._record_l.pack()

        self._record_f = tk.Frame(self._root)



        self._html_f = tk.Frame(self._root)


    def add_to_editor(self):
        text = self._e.get()
        self._editor.add_location_dict(text)
        self._record_num += 1
        self._record_l.config(text = "当前录入总数: " + str(self._record_num))
        self._e.delete(0,'end')


    def see_record(self):
        self._record_f.destroy()
        self._record_f = tk.Frame(self._root)
        self._record_f.pack()
        for location in self._editor.get_dict().keys():
            tk.Label(self._record_f, text = location + " :" + str(len(self._editor.get_dict().get(location, "")))).pack()


    def generate_html(self):
        content = self._editor.encode()
        f = open("html_code.txt", 'w+')
        f.write(content)
        f.close()
        self.create_html_button()

    def create_html_button(self):
        self._html_f.destroy()
        self._html_f = tk.Frame(self._root)

        self._html_f.pack()
        tk.Button(self._html_f, text="打开html文件", command = self.open_txt).pack()

    def open_txt(self):

        os.system("open html_code.txt")


if __name__ == '__main__' :
    root = tk.Tk()
    app = APP(root)
    root.mainloop()

