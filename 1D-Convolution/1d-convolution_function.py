import numpy as np

def convolve_1d(signal, kernel):
    kernel = kernel[::-1]
    return [
        np.dot(
            signal[max(0,i):min(i+len(kernel),len(signal))],
            kernel[max(-i,0):len(signal)-i*(len(signal)-len(kernel)<i)],
        )
        for i in range(1-len(kernel),len(signal))
    ]

res = []

res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [ -1, 0, 1]))
res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, 0, 1, 1]))
res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, 0, 1, 1, 1]))
res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, 0, 1, 1, 1, 1]))
res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1]))
res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1]))
# res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 1]))
# res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1]))
# res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# res.append(convolve_1d([0, 0, 0, 5, 10, 15, 15, 15, 15, 10, 5, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

for r in res:
    print(r)