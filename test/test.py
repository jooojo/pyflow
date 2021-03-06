﻿"""test module"""

from __future__ import print_function

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../../')
    from numpy.testing import assert_equal
    import cv2
    import pylab
    import pyflow

    flow = pyflow.read_flow_file(r"flow10.flo")
    pyflow.write_flow_file("test.flo", flow)
    g = pyflow.read_flow_file(r"test.flo")

    assert_equal(flow, g)

    img = pyflow.flow_to_color(flow)
    pylab.imshow(img)
    pylab.show()

    pylab.imshow(pyflow.show_color_scheme())
    pylab.show()

    prev_frame = cv2.imread("frame10.png")
    next_frame = cv2.imread("frame11.png")
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)
    fbflow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, 0.5, 3, 15, 3, 5, 1.2, 0)

    print(pyflow.calc_epe_stat(fbflow, flow))
