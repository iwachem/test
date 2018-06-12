# -*- coding: utf-8 -*-

import tensorflow as tf

a = tf.constant(3, name='constant1')
b = tf.Variable(0, name='constant2')
add = tf.add(a, b)
assign = tf.assign(b, add)
'''
tr.assign:
assign add to be and return add
'''
c = tf.placeholder(tf.int32, name='input')
mul = tf.multiply(assign, c)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        print(sess.run(mul, feed_dict={c: 3}))
