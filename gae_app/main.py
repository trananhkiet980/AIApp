# -*- coding: utf-8 -*-
import webapp2
import time
from google.appengine.api import memcache

class MainPage(webapp2.RequestHandler):
    def get(self):
        # 1. Định nghĩa một khóa (key) cho dữ liệu cần lưu cache
        cache_key = "my_expensive_query_result"
        
        # 2. Thử lấy dữ liệu từ Memcache
        data = memcache.get(cache_key)
        
        # 3. Kiểm tra xem dữ liệu có tồn tại trong cache không
        if data is not None:
            source = "Từ Memcache (Nhanh)"
        else:
            # Nếu không có trong cache, thực hiện "truy vấn" dữ liệu thật (mô phỏng)
            source = "Từ Database/Truy vấn gốc (Chậm)"
            # Giả lập một kết quả truy vấn là thời gian hiện tại
            data = "Dữ liệu được tạo lúc: " + str(time.strftime("%Y-%m-%d %H:%M:%S"))
            
            # Lưu kết quả vào Memcache trong 60 giây để dùng cho các lần gọi sau
            memcache.add(key=cache_key, value=data, time=60)
            
        # 4. Trả kết quả hiển thị ra màn hình cho người dùng
        self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        self.response.write("Nguồn dữ liệu: %s\n" % source)
        self.response.write("Nội dung: %s" % data)

# Đăng ký URL mapping với template webapp2
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)