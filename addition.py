import os
import tensorflow as tf

#tells tensorflow to output minimal log messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#defining computational graph

"""
Created two nodes called X and Y that'll hold 
data type of float32 and will be called X and
Y respectively. 
"""
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

#The addition node
addition = tf.add(X, Y, name="addition")

#creating session to execute operations in a graph
with tf.Session() as session:

    #running the session and specifying that we need to run
    #the addition node and for which the session would need 
    #two arguments that will be fed as dict (feed_dict)
    result = session.run(addition, feed_dict={X: [1], Y: [4]})
    print(result)
