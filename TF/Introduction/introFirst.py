import tensorflow as tf

print("\n================================================================================================\n")

rank1_tensor = tf.Variable(["String"], tf.string)

print(rank1_tensor)
print(tf.rank(rank1_tensor))
print(rank1_tensor.shape)


print("\n==================================================\n")

rank2_tensor = tf.Variable([["first", "second"], ["third", "fourth"]])

print(rank2_tensor)
print(tf.rank(rank2_tensor))
print(rank2_tensor.shape)


print("\n==================================================\n")

rank3_tensor = tf.Variable([[["first"], ["Second"]], [["Third"], ["Fourth"]], [["Fifth"], ["Sixth"]]])

print(rank3_tensor)
print(tf.rank(rank3_tensor))
print(rank3_tensor.shape)
