import time
import os

lyrics = [
    "nắng mang em đi rồi 🙁",
    "em để lại đớn nhau muôn phần 🙁",
    "đã lỡ buông nhau rã rời",
    "thôi thì xa phải đành cách xa ! 🙁",
    "nhớ nhau bao nhiêu phần",
    "cũng đâu thể tìm thấy nhau !",
    "cách xa nhau làm gì ?",
    "để giờ đây phải chịu đớn đau thêm phần… 🙁"
]

for line in lyrics:
    os.system('cls' if os.name == 'nt' else 'clear')  # Xoá màn hình
    print("\n🎶 " + line)
    time.sleep(3)  # Đợi 3 giây trước khi chuyển dòng

print("\n🎵 Kết thúc đoạn hát.")
