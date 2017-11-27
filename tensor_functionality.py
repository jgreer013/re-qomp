import tensorflow as tf
import read_answer_set as ras
from numpy import around

# Done using tensorflow mnist tutorial:
# https://www.tensorflow.org/get_started/mnist/beginners

def trainTF(training_data, test_data, training_steps=200):

  learning_rate = 0.5
  
  input_tf_length = training_data[0][0].shape[1]*2
  print input_tf_length
  
  x = tf.placeholder(tf.float32, [None, input_tf_length])
  W = tf.Variable(tf.random_normal([input_tf_length, 2]))
  b = tf.Variable(tf.random_normal([1]))
  
  y = tf.nn.softmax(tf.matmul(x, W) + b)
  
  y_ = tf.placeholder(tf.float32, [None, 2])
  
  cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
  
  train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
  
  sesh = tf.InteractiveSession()
  
  tf.global_variables_initializer().run()
  
  testx, testy = ras.getNonRandomBatch(test_data, len(test_data))
  for step in range(training_steps):
    bx, by = ras.getRandomBatch(training_data, 100)
    
    if (step + 1 % 100 == 0):
      learning_rate = learning_rate / 2
      train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
    
    _, crossval = sesh.run([train_step, cross_entropy], feed_dict={x: bx, y_: by})
    #correct_pred = tf.equal(tf.Print(tf.round(y), [tf.round(y)]), tf.Print(tf.round(y_),[tf.round(y_)]))
    correct_pred = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    predictions = tf.argmax(y,1)
    a, preds = sesh.run([acc, predictions], feed_dict={x: testx, y_: testy})
    print 'Run {} {}'.format(step, a)
    #print crossval
    
  a, preds = sesh.run([acc, predictions], feed_dict={x: testx, y_: testy})
  
  print 'Final Accuracy: {}'.format(a)
  
  
  return preds
  
  
  
  
  
