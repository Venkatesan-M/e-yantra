import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/venkatesan/e-yantra/tf2_ws/install/learning_tf2_py'
