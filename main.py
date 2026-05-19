import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def main():
    # 1. 创建应用程序实例
    app = QApplication(sys.argv)

    # 2. 创建主窗口
    window = QWidget()
    window.setWindowTitle("Hello World - PyQt6")
    window.resize(300, 200)

    # 3. 创建一个布局和标签
    layout = QVBoxLayout()
    label = QLabel("Hello, World! 👋")

    # 将标签添加到布局中
    layout.addWidget(label)

    # 将布局设置到窗口
    window.setLayout(layout)

    # 4. 显示窗口
    window.show()

    # 5. 启动应用程序的事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

