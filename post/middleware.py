from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

BLOCKIP = [
    '127.0.0.1',
    '192.168.0.4'
    '10.0.123.45'
]


class BlockIP(MiddlewareMixin):
    @staticmethod
    def is_blocked_ip(ip):
        return ip in BLOCKIP

    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']
        if self.is_blocked_ip(ip):
            return render(request, 'blockers.html')
        return
