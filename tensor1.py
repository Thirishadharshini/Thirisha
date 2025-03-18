import tensorflow as tf

# TensorFlow 2.x style code, no session needed
node1 = tf.constant(3.0)
node2 = tf.constant(5.0)
node3 = tf.add(node1, node2)  # This operation executes immediately

print("Sum of node1 and node2 is:", node3.numpy())
print(tf.__version__)
