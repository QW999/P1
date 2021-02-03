import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())

import numpy as np
import time
#
# # Prepare data
# np.random.RandomState(1)
# arr = np.random.randint(0, 10, size=[1000000, 25])
# data = arr.tolist()
#
# # print(data)
# print(data[:5])
#
# def howmany_within_range(row, minimum=4, maximum=8):
#     """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
#     count = 0
#     for n in row:
#         if minimum <= n <= maximum:
#             count = count + 1
#     return count
#
#
# # Solution Without Paralleization
#
# start = time.time()
#
# results = []
# for row in data:
#     results.append(howmany_within_range(row, minimum=4, maximum=9))
#
# end = time.time()
#
# # print(results)
# print("Time taken without paralelization: {}".format(end-start))
#
# # Solution With Paralleization
#
# ## Parallelizing using Pool.apply()
#
# # Step 1: Init multiprocessing.Pool()
# # pool = mp.Pool(2)
#
# # # Step 2: `pool.apply` the `howmany_within_range()`
# # results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
# # # Step 3: Don't forget to close
# # pool.close()
#
# # print(results[:10])
#
# pool = mp.Pool(4)
#
# start = time.time()
#
# results = pool.map(howmany_within_range, data)
#
# end = time.time()
#
# pool.close()
# print("Time taken with paralelization: {}".format(end-start))
#
# # print(results[:10])
#
# # Parallelizing with Pool.starmap()
#
# pool = mp.Pool(4)
#
# ("Time taken with paralelization: {}".format(end - start))
#
# pool.close()
# start  =time.time()
# results = pool.starmap(howmany_within_range, [(row, 3, 10) for row in data])
# end = time.time()
#
# print

# print(results[:10])

# Homework:
# 1. read the rest of the pdf document tha remained

# 2.Define a list  of 20 url resources (favorite sites that you visit most often).

# you have the following code:

import time
import urllib.request as urllib

def millis():
  return int(round(time.time() * 1000))

def http_get(url):
    start_time = millis()
    try:
        result = {"url": url, "data": urllib.urlopen(url, timeout=7).read()}
        print(url + " took " + str(millis() - start_time) + " ms")
        return result
    except Exception as ex:
        print("Attempt failed for: {}. Got Exception {}".format(url, ex))
        return dict()

# define the code that would make use of this http_get funtion and run it in parallel for the list of urls that you have defined. Select the fastest method to accomplish your task


if __name__ == '__main__':
    import sys
    thread_num = int(sys.argv[1])
    url_list = [
'http://www.python.org',
'http://www.python.org/about/',
'http://www.python.org/doc/',
'http://www.python.org/download/', 'http://www.web2py.com/', 'http://www.web2py.com/init/default/documentation',
"https://amazon.com", "https://ebay.com", 'http://www.999.md', 'http://point.md', 'https://www.facebook.com',
"https://agora.md", "https://unimedia.md", "https://yahoo.com"

]
    pool = mp.Pool(thread_num)
    start=time.time()
    results = pool.map(http_get, url_list)
    pool.close()
    pool.join()
    end = time.time()
    print("Time taken with paralelization: {}".format(end - start))