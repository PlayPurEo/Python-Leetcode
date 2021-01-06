# author : 'wangzhong';
# date: 23/12/2020 16:51

"""
编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

如果是有效的 IPv4 地址，返回 "IPv4" ；
如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。
"""


class Solution:
    def validIPAddress(self, IP: str) -> str:
        NEITHER = "Neither"
        IPV4 = "IPv4"
        IPV6 = "IPv6"

        def validIP4(IP: str) -> str:
            nums = IP.split(".")
            for i in nums:
                if len(i) == 0 or len(i) > 3:
                    return NEITHER
                if i[0] == '0' and len(i) != 1 or not i.isdigit() or int(i) > 255:
                    return NEITHER
            return IPV4

        def validIP6(IP: str) -> str:
            nums = IP.split(':')
            hexdigits = '0123456789abcdefABCDEF'
            for x in nums:
                if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                    return NEITHER
            return IPV6
        if IP.count('.') == 3:
            return validIP4(IP)
        elif IP.count(':') == 7:
            return validIP6(IP)
        else:
            return NEITHER


if __name__ == '__main__':
    s = "fafsfa::fadsads"
    a = s.split(":")
    print(a)
