from datetime import datetime
import numpy as np
import sys
print(sys.version)
start_time = datetime.now()
matrix_size = 10000

matrix_a = np.random.rand(matrix_size,matrix_size)
matrix_b = np.random.rand(matrix_size,matrix_size)

matrix_c = np.dot(matrix_a,matrix_b)

end_time = datetime.now()

executeion_time = end_time - start_time
print(f"Matrix multiplication execution time: {executeion_time}")