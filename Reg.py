import re


# 从输入的字符串中匹配正确的手机号码
class Reg():
    def __init__(self):
        self.right_phone_num = '13590210076'
        self.wrong_phone_num = '12345678901'
        self.wrong_phone_num_tail = '135902100761'
        self.wrong_phone_num_head = '1135902100761'
        self.multi_phone_num = '12790210676,11990210676,10990210676,13590210676,13590210676, 18996720675, 18996720675, 12345678910'
        self.reg = '1[3,5,7,8][0-9]{9}'
        self.pattern = re.compile(self.reg)
        self.test_html = '下面才是正文<pre style="display:inline;" class="content">看“空城计”的三个阶段:“哇，诸葛亮好厉害”；“假的，没意思”；“兔死狗烹，弹尽弓藏……不愧是孔明”</pre>'

    def test_match_search(self):
        print('Right Phone Number=========================')
        print(re.match(self.pattern, self.right_phone_num))
        print(re.search(self.pattern, self.right_phone_num))
        print('Wrong Phone Number=========================')
        print(re.match(self.pattern, self.wrong_phone_num))
        print(re.search(self.pattern, self.wrong_phone_num))
        print('Wrong Phone Number Tail=========================')
        print(re.match(self.pattern, self.wrong_phone_num_tail))
        print(re.search(self.pattern, self.wrong_phone_num_tail))
        print('Wrong Phone Number Head=========================')
        print(re.match(self.pattern, self.wrong_phone_num_head))
        print(re.search(self.pattern, self.wrong_phone_num_head))
        print('Multi Phone Number=========================')
        print(re.match(self.pattern, self.multi_phone_num))
        print(re.search(self.pattern, self.multi_phone_num))

    def test_findall(self):
        print('Find all Multi Phone Number=========================')
        phone = re.findall(self.pattern, self.multi_phone_num)
        print(','.join(phone))

    def test_sub(self):
        print("Sub =============================")
        print(re.subn(self.pattern, '正确的电话号码', self.multi_phone_num))
        print(re.sub(self.pattern, '正确的电话号码', self.multi_phone_num))
        print(re.subn(self.pattern, '正确的电话号码', self.multi_phone_num, 2))
        print(re.sub(self.pattern, '正确的电话号码', self.multi_phone_num, 2))

    def test_greedy(self):
        print('Greedy===========================')
        print(re.findall(re.compile('<.*>'), self.test_html))
        print('No Greedy===========================')
        print(re.findall(re.compile('<.*?>'), self.test_html))

    def test_capture(self):
        self.words = '诸葛亮就是诸葛孔明不是诸葛瑾'
        reg_capture = '诸葛(亮|孔明)'
        reg_no_capture = '诸葛(?:亮|孔明)'
        reg_no_capture2 = '诸葛(?=亮|孔明)'
        reg_no_capture3 = '诸葛(?!亮|孔明)'
        self.reverse_words = '大司马'
        self.reverse_wrong_words = '小司马'
        reg_no_capture_reverse = '(?<=大)司马'
        reg_no_capture_inorder = '司马(?=大)'
        reg_no_capture_reverse_negative = '(?<!大)司马'
        print("Capture===========================")
        print(re.findall(re.compile(reg_capture), self.words))
        print("No Capture========================")
        print(re.findall(re.compile(reg_no_capture2), self.words))
        print("反向肯定预查============================")
        print(re.findall(re.compile(reg_no_capture_reverse), self.reverse_words))
        print(re.findall(re.compile(reg_no_capture_reverse), self.reverse_wrong_words))
        print("反向否定预查============================")
        print(re.findall(re.compile(reg_no_capture_reverse_negative), self.reverse_words))
        print(re.findall(re.compile(reg_no_capture_reverse_negative), self.reverse_wrong_words))
        print("正向预查=============================")
        print(re.findall(re.compile(reg_no_capture_inorder), self.reverse_words))

    def test_innerHTML(self):
        print('使用正则提取html innerHTML===================')
        print(re.findall(re.compile('(?<=<pre style="display:inline;" class="content">).*(?=</pre>)'), self.test_html))


if __name__ == '__main__':
    reg = Reg()
    # reg.test_match_search()
    # reg.test_findall()
    # reg.test_sub()
    # reg.test_greedy()
    # reg.test_capture()
    reg.test_innerHTML()
