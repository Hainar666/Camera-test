# 运行前在终端输入：pip install opencv-python （这是运行库）
import cv2  # 引入 OpenCV 库（负责摄像头、图像读取与显示等功能）

# ---------- 打开摄像头 ----------
cap = cv2.VideoCapture(0)
# 上面这行：创建一个 VideoCapture 对象并尝试打开索引为 0 的摄像头（通常是内置摄像头或第一个 USB 摄像头）。
# 如果你有多个摄像头，可以改成 1、2 来尝试其它设备；也可以传入视频文件路径以打开视频文件。

# （可选）向摄像头“请求”分辨率（这是申请，摄像头/驱动可能不完全服从）
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)   # 请求宽度为 1280
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)   # 请求高度为 720

# ---------- 主循环：不断读取并显示每一帧 ----------
while True:
    ret, frame = cap.read()
    # cap.read() 会返回两个值：
    # - ret: 布尔值，表示这一帧是否成功读取到（True 表示成功，False 表示失败或流断开）
    # - frame: 图像矩阵（如果 ret 为 True，则是当前帧的像素数据；如果为 False，frame 可能为空）
    if not ret:
        # 读取失败时退出循环（避免进入死循环或显示空画面）
        break

    cv2.imshow("Camera", frame)
    # 把读取到的 frame 在一个名为 "Camera" 的窗口里显示出来。
    # imshow 不会改变帧的内容，只负责把像素画到窗口上；窗口大小会和 frame 的分辨率一致。

    # 等待键盘输入，参数是等待的毫秒数（这里 1 毫秒），并用位运算取最低 8 位与 27 比较以检测 Esc 键。
    # waitKey 的返回值包含了键码（在不同平台上有差异），常用写法是 & 0xFF 去掉高位干扰。
    if cv2.waitKey(1) & 0xFF == 27:  # 27 是 Esc 键的 ASCII 码
        # 如果检测到 Esc（按下），就跳出循环，进入资源释放阶段
        break

# ---------- 退出前的清理：释放摄像头并关闭所有窗口 ----------
cap.release()           # 释放摄像头设备占用（必须做，不然摄像头可能被占着无法被其他程序使用）
cv2.destroyAllWindows() # 关闭所有由 OpenCV 打开的窗口，清理 GUI 资源